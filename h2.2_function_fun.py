#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Ivan Zemlyaniy aka shaolinfm
# @Date:   2015-06-14 22:40:03
# @Last Modified by:   Ivan Zemlyaniy
# @Last Modified time: 2015-06-15 01:38:17
#
#HarveyMuddX: CS005x CS For All: Introduction to Computer Science and Python Programming
#FUNCTION FUN!
#Homework 2.2 - FUNCTIONS TO WRITE

import math

def tpl(x):
    """ output: tpl returns thrice its input
         input x: a number (int or float)
    """
    return x*3

def sq(x):
    """output: returns square of its input
        input x: a number (float)
    """
    return x*x

def interp(low,hi,fraction):
    """ interpolate returns the fraction of the difference between low and hi plus low
          inputs are low, hi, and fraction (all int or float)
    """
    return ((hi-low)*fraction)+low

def checkends(s):
    """this function takes in a string s and returns True if the first character in s is the same as the last character in s. It returns False otherwise.
    """
    if s[0] == s[-1]:
        return True
    else:
        return False

def flipside(s):
    """function flipside(s), which takes in a string s and returns a string whose first half is s's second half and whose second half is s's first half.
    """
    mid = len(s) / 2
    return s[mid:] + s[0:mid]

def convertFromSeconds(s):
    """function takes in a nonnegative integer number of seconds s and returns a list of converted second in to usual format [days, hours, minutes, seconds]
    """
    days = s//(24*60*60)
    hours = (s%(24*60*60))//(60*60)
    minutes = ((s%(24*60*60))%(60*60))//60
    seconds = ((s%(24*60*60))%(60*60))%60
    return [days, hours, minutes, seconds]

def front3(str):
    """ function returnes multiplied on 3 first 3 characters of giving string
    """
    return str[:3]*3


if __name__ == "__main__":
    pass
