#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
-------------------------------------------------
   File Name：     0005
   Author :       zhang
   date：          19-12-25

   pip install Pillow
-------------------------------------------------
"""
import glob,os
from PIL import Image

size = 1136,640

def thumbnail_pic(path):
    for infile in glob.glob(path):
        file,ext = os.path.splitext(infile)
        im = Image.open(infile)
        im.thumbnail(size)
        print(im.format, im.size, im.mode)
        im.save(file + ".thumbnail", "JPEG")
    print("Done")

if __name__ == '__main__':
    path = r"img/*.jpg"
    thumbnail_pic(path)