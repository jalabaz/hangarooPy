# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 15:04:26 2019

@author: jalabaz
"""

def isWordGuessed(secretWord, lettersGuessed):
    for x in secretWord:
        if x in lettersGuessed:
            i = 1
            continue
        else:
            return False
            i = 0
    if i != 0:
        return True
