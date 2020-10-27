from classy_vision.dataset import ImagePathDataset, register_dataset
from classy_vision.dataset.transforms import build_transforms

@register_dataset("ds_film")
class Film(ImagePathDataset):
    def __init__(self, batchsize_per_replica, shuffle, transforms, num_samples, image_folder):
        super().__init__(batchsize_per_replica, shuffle, transforms, num_samples, image_folder)
        
    @classmethod
    def from_config(cls, config):        
        transforms = config.get("transforms")
        transforms = build_transforms(transforms)
        return cls(
            batchsize_per_replica=config["batchsize_per_replica"],
            shuffle=config["use_shuffle"],
            transforms = transforms,
            num_samples=config["num_samples"],
            image_folder=config["image_folder"]
        )


# =============================================================================
# from classy_vision.dataset import build_dataset
# from classy_vision.dataset.transforms import build_transforms, ApplyTransformToKey
# import torch
# from torchvision import transforms
# 
# image_transform = transforms.Compose([
#         #transforms.Resize(256),
#         #transforms.CenterCrop(224),
#         transforms.ToTensor(),
#         #transforms.Normalize(mean=[0.485, 0.456, 0.406], std=[0.229, 0.224, 0.225]),
# ])
# 
# transform = ApplyTransformToKey(transform=image_transform, key="input")
# 
# dataset_config = {
#     "name": "ds_steel",
#     "batchsize_per_replica":5,
#     "shuffle": True,
#     #"transforms": [{"name": "Normalize", "mean": [0.485, 0.456, 0.406], "std": [0.229, 0.224, 0.225]}],
#     "transforms":transform,
#     "num_samples":5,
#     "image_folder": "steel"
# }
# 
# steelds = build_dataset(dataset_config)
# 
# iterator = steelds.iterator(
#     shuffle_seed=1,
#     epoch=0,
#     num_workers=0,  # 0 indicates to do dataloading on the master process
#     pin_memory=False,
#     multiprocessing_context=None,
# )
# 
# from matplotlib import pyplot as plt
# from torchvision.transforms.functional import to_pil_image
# 
# #assert isinstance(iterator, torch.utils.data.DataLoader)
# for sample in iter(iterator):
# 	#print("input: ", sample["input"].shape)
# 	for i in range(sample["input"].shape[0]):
# 		plt.imshow(to_pil_image(sample["input"][i]))
# 		plt.show()
# 	print("target: ", sample["target"])
# 
# 
# from classy_vision.dataset.classy_synthetic_image import SyntheticImageDataset
# =============================================================================

