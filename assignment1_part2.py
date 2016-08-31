#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Tracks books and authors"""


class Book:
    def __init__( self, author = '', title = '' ):
        self.a = author
        self.t = title
        return

    def display( self ):
        """prints the book title and author"""
        print "%s, written by %s" % (self.a, self.t)
        return

booka = Book('Of Mice and Men', 'John Steinbeck')
bookb = Book('To Kill a Mockingbird', 'Harper Lee')

booka.display()
bookb.display()
