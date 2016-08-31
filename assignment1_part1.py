#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tests divisibility of numbers in a list"""


def listDivide( numbers, divide = 2 ):
"""numbers is a list""" 
"""divide is the divisor"""
"""returns the number of list items that are divisble by the divisor"""
int divisibles
for anumber in numbers:
if anumber % divide == 0:
divisibles += 1 
return divisibles

"""class ListDivideException"""

def testListDivide( ):
"""raise exception if any fail"""
listDivide([1,2,3,4,5])
listDivide([2,4,6,8,10])
listDivide([30, 54, 63,98, 100], divide=10)
listDivide([])
listDivide([1,2,3,4,5], 1)
return

testListDivide
