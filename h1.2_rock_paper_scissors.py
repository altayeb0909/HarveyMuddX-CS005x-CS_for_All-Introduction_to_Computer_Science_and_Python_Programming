# python 2

#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Ivan Zemlyaniy aka shaolinfm
# @Date:   2015-06-01 15:24:12
# @Last Modified by:   shaolinfm
# @Last Modified time: 2015-06-03 09:21:37


"""
Homework 1, Problem 2 - "Rock, Paper, Scissors" Game

This is simple implementation of famous game called "Rock, Paper, Scissors".
"""
import random

def rock_paper_scissors():

    variations = ("rock", "paper", "scissors")
    user = str(raw_input("Choose your weapon: "))
    computer = variations[random.randint(0,2)]

    if computer == user:
        print "The user chose %s" % user
        print "The computer chose %s" % computer
        print "It's a Tie!"

    elif (computer == "scissors" and user == "paper") or (computer == "paper" and user == "rock") or (computer == "rock" and user == "scissors"):
        print "The user chose %s" % user
        print "The computer chose %s" % computer
        print "Computer Win!"

    else:
        print "The user chose %s" % user
        print "The computer chose %s" % computer
        print "User Win!"

if __name__ == '__main__':
    rock_paper_scissors()


