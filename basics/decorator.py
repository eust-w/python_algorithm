#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""@author:longt
@file:decorator.py
@time:2020/03/02
"""


flag = 0

if flag:
    # f1 is a decorator function
    def f1(_):
        print('1')
        # _()
        print('2')
        return '11'

    @f1
    def f2():
        print('3')
        return '12'
    print(f1)
    print(f2)
else:
    def a(_):
        print('1')
        _()
        print('2')
        return '13'

    def b():
        print('3')
        return '14'
    b = a(b)
    # print(c)
    print(a)
    print(b)
