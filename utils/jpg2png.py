import os
import sys

from PIL import Image

if len(sys.argv) < 3:
    print("Usage: python jpg2png.py [path] [dest]")
    sys.exit(1)

path = sys.argv[1]
dest = sys.argv[2]

def pixel_process(img):
    img = img.convert('RGBA')
    L, H = img.size
    datas = img.getdata()
    new_data = list()
    for i in datas:
        new_data.append(i)
    img.putdata(new_data)
    return img

if not os.path.exists(dest):
    os.mkdir(dest)

files = os.listdir(path)
index = 1
for file in files:
    if file == ".DS_Store":
        continue
    full_path = os.path.join(path, file)
    dest_path = os.path.join(dest, "%d.png" % index)
    img = Image.open(full_path)
    new_img = pixel_process(img)
    new_img.save(dest_path, "PNG")
    index += 1

print("Done, converted %d files." % index)
