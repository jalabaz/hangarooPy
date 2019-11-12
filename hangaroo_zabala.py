# -*- coding: utf-8 -*-
"""
Created on Mon Nov 11 15:04:26 2019

@author: jalabaz
"""

from isWordGuessed_zabala import isWordGuessed
from getGuessedWord_zabala import getGuessedWord
from getAvailableLetters_zabala import getAvailableLetters

def Hangaroo(secretWord):
    import string
    lss = 0
    lettersGuessed = [' ']
    mistakesMade = 0
    print('Secret word: ', getGuessedWord(secretWord, lettersGuessed))
    print('Letters Left: ', getAvailableLetters(lettersGuessed))
    while isWordGuessed(secretWord, lettersGuessed) == False:
        i = 1
        while i > 0:
            ltr = input("PICK A LETTER: ")
            if ltr[0].isupper():
                ltr = ltr[0].swapcase()
            if ltr[0] in string.ascii_lowercase:
                i = 0
            else:
                print('Wrong output! Must be a letter, try again!')
            if ltr[0] in lettersGuessed and ltr[0] != ' ':
                print('That letter has already been guessed! Try again!')
                i = 1
        lettersGuessed.append(ltr[0])
        if ltr[0] not in secretWord:
            print('Wrong! :(\n')
            mistakesMade += 1;
            if mistakesMade == 5:
                lss = 1
                break
        else:
            print('Nice!\n')
        print('Lives: ', (5-mistakesMade))
        print('Secret word: ', getGuessedWord(secretWord, lettersGuessed))
        print('Letters Left: ', getAvailableLetters(lettersGuessed))
    if lss != 1:
        print('\n\nCongratulations! You guessed the secret word!')
    else:
        for x in secretWord:
            if x is ' ':
                secretWord = secretWord.replace(x, '')
        print('\nThe kangaroo died! You lost! Secret word:\n\t', secretWord)
        
Hangaroo('p y t h o n')