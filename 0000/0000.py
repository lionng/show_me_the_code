#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
-------------------------------------------------
   File Name：     0000
   Author :       zhang
   date：          19-12-10
-------------------------------------------------
"""
from PIL import Image,ImageDraw,ImageFont

im = Image.open("12.jpg")

print(im.format,im.size,im.mode)

draw = ImageDraw.Draw(im)
myfont = ImageFont.truetype('arial.ttf',size=80)

color = "#ff0000"

draw.text((400,40),'7',font=myfont,fill=color)

im.save('result.jpg','jpeg')
