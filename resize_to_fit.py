
from sys import argv
import os
from PIL import Image

semester = argv[1]
for image in os.listdir(semester):
    path = os.path.join(semester, image)
    im = Image.open(path)
    print(path, im.size)
    if im.size[0] <= 150:
        continue
    wratio = 150 / im.size[0]
    im = im.resize((int(wratio * im.size[0]), int(wratio * im.size[1])))
    im.save(path)
