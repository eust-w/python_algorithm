#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""@author:longt
@file:decorator2.py
@time:2020/03/02
"""
import time


def timeit(_):
    start_time = time.time()
    _()
    end_time = time.time()
    return end_time - start_time


@timeit
def f1():
    time.sleep(1)
    print('f1')


@timeit
def f2():
    time.sleep(2)
    print('f2')

# print(f1)
# print(f2)
f1()
f2()
