import torch.nn as nn

from classy_vision.models import ClassyModel, register_model


@register_model("m_base")
class MyModel(ClassyModel):
    def __init__(self, num_classes):
        super().__init__()
        
        # Average all the pixels, generate one output per class
        self.avgpool = nn.AdaptiveAvgPool2d((1, 1))
        num_channels = 1
        self.fc = nn.Linear(num_channels, num_classes)

    @classmethod
    def from_config(cls, config):
        # This method takes a configuration dictionary 
        # and returns an instance of the class. In this case, 
        # we'll let the number of classes be configurable.
        return cls(num_classes=config["num_classes"])
        
    def forward(self, x):
        # perform average pooling
        out = self.avgpool(x)

        # reshape the output and apply the fc layer
        out = out.reshape(out.size(0), -1)
        out = self.fc(out)
        return out
    
    