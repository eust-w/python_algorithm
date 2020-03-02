#!/usr/bin/python
# -*- coding: UTF-8 -*-
"""@author:longt
@file:bubble_sort.py
@time:2020/03/02
"""
import random


def bubble_sort(sol: list)->list:
    for i in range(len(sol)):
        flag = 1
        for j in range(len(sol)-i-1):
            if sol[j] > sol[j+1]:
                sol[j], sol[j+1] = sol[j+1], sol[j]
                flag = 0
        if flag:
            return sol
    return sol


if __name__ == '__main__':
    q = int(input('please enter list size:'))
    list1 = list(range(q))
    random.shuffle(list1)

    list2 = bubble_sort(list1)
    list3 = sorted(list1)

    print(list2 == list3)
    print('\n', list2, '\n'.ljust(0), list3)
