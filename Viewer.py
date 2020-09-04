import imageio
import json
import napari
import sys

# assign the path to the montage file
args = sys.argv
path_to_montage = args[1] + '\\bestFocus\\' + args[2]
path_to_channelNames = args[1] + '\\channelNames.txt'
path_to_json = args[1] + '\\Experiment.json'
lines = []
with open(path_to_channelNames) as f:
    lines = f.readlines()
with open(path_to_json) as json_file:
    experimentJson = json.load(json_file)
num_cycles = experimentJson['num_cycles']
num_channels = len(experimentJson['channel_names'])
region_stack = imageio.volread(path_to_montage)
x = 0
with napari.gui_qt():
    viewer = napari.Viewer()
    for cy in range(num_cycles):
        for ch in range(num_channels):
            viewer.add_image(region_stack[cy, ch], blending='additive', gamma=0.85, visible=False, name=lines[x])
            x = x+1
