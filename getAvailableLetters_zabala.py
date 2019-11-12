# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 16:42:58 2019

@author: Admin
"""

def getAvailableLetters(lettersGuessed):
    import string
    availableLetters = string.ascii_lowercase
    for x in availableLetters:
        if x in lettersGuessed:
            availableLetters = availableLetters.replace(x, '_')
    return availableLetters
