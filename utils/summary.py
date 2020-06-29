import os
import sys

if len(sys.argv) < 3:
    print("Usage: python summary.py [origin] [label]")
    sys.exit(1)

origin = sys.argv[1]
label = sys.argv[2]

files = os.listdir(origin)
index = 1
result = ""
for file in files:
    if file == ".DS_Store":
        continue
    filename = file.replace(".jpg", ".png")
    png_path = os.path.join(label, filename)
    if filename.startswith("epoch"):
        png_name = filename.split("-")[0]
        result += "%s;%s.png\n" % (file, png_name)
        index += 1
    else:
        if os.path.exists(png_path):
            result += "%s;%s\n" % (file, filename)
        index += 1

with open("train.txt", "w") as file:
    file.write(result)

print("Done, found %d groups of images." % index)
