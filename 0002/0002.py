#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""
-------------------------------------------------
   File Name：     0002
   Author :       zhang
   date：          19-12-22

   pip install PyMySQL
-------------------------------------------------
"""
import random
import pymysql

conn = pymysql.connect(host='127.0.0.1',port=3306,user='root',passwd='passwd',db='python_pract',charset='utf8')
cur = conn.cursor()

try:
    for i in range(0,200):
        string = ''
        for j in range(0,4):
            string = string + str(random.randint(0,9))
        # print(string)
        sql = "INSERT INTO xiaofeng(active_code) VALUES('{}')".format(string)
        print(sql)
        cur.execute(sql)
    conn.commit()  #notice
    print("success")
except:
    print("rollback")
    conn.rollback()
finally:
    print("close")
    cur.close()
    conn.close()