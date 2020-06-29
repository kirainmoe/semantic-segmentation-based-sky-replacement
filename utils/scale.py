import os
import sys
import numpy as np
from PIL import Image

if len(sys.argv) < 5:
    print("Usage: python scale.py [image_path] [destination_path] [target_width] [target_height]")
    sys.exit(1)

image_path = sys.argv[1]
destination_path = sys.argv[2]
target_width = int(sys.argv[3])
target_height = int(sys.argv[4])

if not os.path.exists(destination_path):
    os.mkdir(destination_path)

total = 0
path_files = os.listdir(image_path)
for file in path_files:
    try:
        full_path = os.path.join(image_path, file)
        img = Image.open(full_path)
        output = img.resize((target_width, target_height))
        save_path = os.path.join(destination_path, file)
        output.save(save_path)
        total += 1
    except:
        print("Scale error for file %s!" % file)

print("Image scale done, processed %d images." % total)
