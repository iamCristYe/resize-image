from PIL import Image
from pathlib import Path
import re

NEW_SIZE = 1500

pathlist = Path(".").glob("*/*.JPG")
for path in pathlist:
    # print(str(path)[0])
    # print(str(path.name))
    temp = re.findall(r"\d+", str(path.name))
    number = int(temp[0])

    current = Image.open(path)
    width, height = current.size
    # print(width / height)
    if width > height:
        new = current.resize((NEW_SIZE, int(NEW_SIZE * height / width)))
    else:
        new = current.resize((int(NEW_SIZE * width / height), NEW_SIZE))
    new.save(f"{str(path)[0]}-{number}.jpg")
