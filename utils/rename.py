import os
import sys

if len(sys.argv) < 4:
    print("Usage: python reanme.py [path] [dest] [suffix]")
    sys.exit(1)

path = sys.argv[1]
dest = sys.argv[2]
suffix = sys.argv[3]
if len(sys.argv) > 4:
    prefix = sys.argv[4]
else:
    prefix = ""

if not os.path.exists(dest):
    os.mkdir(dest)

files = os.listdir(path)
index = 1
for file in files:
    if file == ".DS_Store":
        continue
    full_path = os.path.join(path, file)
    dest_path = os.path.join(dest, "%s%d.%s" % (prefix, index, suffix))
    os.rename(full_path, dest_path)
    index += 1

print("Done, renamed %d files." % index)
