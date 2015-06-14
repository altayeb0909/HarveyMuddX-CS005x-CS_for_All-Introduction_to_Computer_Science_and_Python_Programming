#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Ivan Zemlyaniy aka shaolinfm
# @Date:   2015-06-01 15:24:12
# @Last Modified by:   Ivan Zemlyaniy
# @Last Modified time: 2015-06-15 01:40:52
#
#Homework 1, Problem 1 - "Four-Fours Puzzle"
#
#This is simple implementation of "Four-Fours Puzzle" described in the January 1964 issue of Scientific American in Martin Gardner's "Mathematical Games" column.".

import os

def four_fours():
    """Function for printing on screen results of Four-Fours Puzzle
    """
    print '"Four-Fours Puzzle"'
    print "Zero is: 4 + 4 - 4 - 4 =", 4 + 4 - 4 - 4
    print "One is: (4 + 4) / (4 + 4) =", (4 + 4) / (4 + 4)
    print "Two is: 4 / 4 + 4 / 4 =", 4 / 4 + 4 / 4
    print "Three is: (4 + 4 + 4) / 4 =", (4 + 4 + 4) / 4
    print "Four is: 4 * (4 - 4) + 4 =", 4 * (4 - 4) + 4
    print "Five is: (4 * 4 + 4) / 4 =", (4 * 4 + 4) / 4
    print "Six is: ((4 + 4) / 4) + 4 =", ((4 + 4) / 4) + 4
    print "Seven is: 44 / 4 - 4 =", 44 / 4 - 4
    print "Eight is: 4 + 4 + 4 - 4 =", 4 + 4 + 4 - 4
    print "Nine is: 4 / 4 + 4 + 4 =",  4 / 4 + 4 + 4
    print

if __name__ == '__main__':

    def clear_terminal_window():
        """Function that clear terminal screen"""

        os.system(['clear','cls'][os.name == 'nt'])

    clear_terminal_window()
    four_fours()

