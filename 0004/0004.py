#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
-------------------------------------------------
   File Name：     0004
   Author :       zhang
   date：          19-12-25
-------------------------------------------------
"""
import re

def count_words(file_path):
    with open(file_path) as file:
        text = file.read()
        words = re.findall(r'[a-zA-Z]+',text)

        print(words)
        set_words = set(words)
        print(set_words)
        print("set_words_len={}".format(len(set_words)))

        count = len(words)
    return count

print(count_words('english.txt'))