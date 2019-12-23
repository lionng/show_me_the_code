#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
-------------------------------------------------
   File Name：     0001
   Author :       zhang
   date：          19-12-22
-------------------------------------------------
"""
import random
for i in range(0,200):
    string = ''
    for j in range(0,4):
        string = string + str(random.randint(0,9))
    print(string)