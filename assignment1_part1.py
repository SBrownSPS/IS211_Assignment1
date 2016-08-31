#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests divisibility of numbers in a list"""


def listDivide( numbers, divide = 2 ):
    """tests divisibility
    :param numbers: numbers is a list
    :param divide: divide is the divisor
    :return: returns the number of list items that are divisble by the divisor
    """
    divisibles = 0
    for anumber in numbers:
        if anumber % divide == 0:
           divisibles += 1
    return divisibles

class ListDivideException(Exception):
    pass

def testListDivide( ):
    """raises exception if any fail"""
    try:
        listDivide([1,2,3,4,5])
    except:
        raise ListDivideException('Unknown Issue')
    try:
        listDivide([2,4,6,8,10])
    except:
        raise ListDivideException('Unknown Issue')
    try:
        listDivide([30,54,63,98,100],divide=10)
    except:
        raise ListDivideException('Unknown Issue')
    try:
        listDivide([])
    except:
        raise ListDivideException('Unknown Issue')
    try:
        listDivide([1,2,3,4,5],1)
    except:
        raise ListDivideException('Unknown Issue')
    return

testListDivide()