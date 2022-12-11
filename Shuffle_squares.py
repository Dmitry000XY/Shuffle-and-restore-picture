from PIL import Image
import numpy as np
import random

# import os
# from pprint import pprint

width = 10000
height = 1

img = Image.open("test.jpg")
img = np.asarray(img)
colors, img_width, img_height = img.shape[::-1]
squ_width, squ_height = img_width // width, img_height // height

# Разрезание картинки
squares = []
for w in range(width):
    for h in range(height):
        tmp = img[h * squ_height:(h + 1) * squ_height, w * squ_width:(w + 1) * squ_width]
        squares.append(tmp)

# Склеивание картинки
random.shuffle(squares)
columns = []
for w in range(width):
    tmp = []
    for h in range(height):
        tmp.extend(squares[h * width + w].tolist())
    columns.append(tmp)

image = []
for row in zip(*columns):
    tmp = []
    for element in row:
        tmp.extend(element)
    image.append(tmp)

image = np.array(image, 'uint8')
im = Image.fromarray(image)
im.show()
