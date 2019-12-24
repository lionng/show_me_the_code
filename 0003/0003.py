#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
-------------------------------------------------
   File Name：     0003
   Author :       zhang
   date：          19-12-24

   linux运行redis指南：https://redis.io/download
   pip install redis
-------------------------------------------------
"""
import redis
import random

r = redis.Redis(host='localhost',port=6379)

for i in range(0,200):
    string = ''
    for j in range(0,4):
        string = string + str(random.randint(0,9))
    print("key:{}  value:{}".format(i,string))
    r.set(i,string)