# https://stackoverflow.com/questions/16010869/plot-a-bar-using-matplotlib-using-a-dictionary
# https://stackoverflow.com/questions/34674558/how-to-change-space-between-bars-when-drawing-multiple-barplots-in-pandas
# https://moonbooks.org/Articles/How-to-add-text-on-a-bar-with-matplotlib-/

from matplotlib import pyplot as plt
import pandas as pd
from matplotlib.patches import Patch

fig, ax = plt.subplots(figsize=(5,4))

data = {'Black': 2522, 'Dust': 1689, 'Stain': 576, 'TakeOff':576, 'UnderGlue':257}
stt = [0,1,2,3,4]
names = list(data.keys())
values = list(data.values())
colors = ['blue', 'orange', 'green', 'red', 'purple']
bar_plot = plt.bar(stt,values,tick_label=names, color=colors, width=0.6)

def autolabel(rects):
    for idx,rect in enumerate(bar_plot):
        height = rect.get_height()
        ax.text(rect.get_x() + rect.get_width()/2., 1.0*height,
                values[idx],
                ha='center', va='bottom', rotation=0)

autolabel(bar_plot)
plt.title('Annotation number of each class ')
plt.savefig("../img/num_of_labels.png", bbox_inches='tight')
