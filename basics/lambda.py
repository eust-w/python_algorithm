#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""@author:longt
@file:lambda.py
@time:2020/03/02
"""

f = [lambda x: x, lambda x: x**2, lambda x: x**3]

for i in f:
    print(i(3))
