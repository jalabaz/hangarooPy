# -*- coding: utf-8 -*-
"""
Created on Tue Nov 12 16:27:19 2019

@author: jalabaz
"""

def getGuessedWord(secretWord, lettersGuessed):
    guessedWord = secretWord
    for x in secretWord:
        if x in lettersGuessed:
            continue
        else:
            if x is ' ':
                continue
            else:
                guessedWord = guessedWord.replace(x, "_")
    return guessedWord