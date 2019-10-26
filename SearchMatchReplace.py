# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import re
    
def replaceWord(filePth, word, wordReplace):
    try:
        openFile = open(filePth)
        
        print("Below are the lines that contains the strings after replacement")
        for line in openFile:
            words = word.split("|")
            for i in words:
                
                if i in line:
                    print(re.sub(i,wordReplace,line))
 
        openFile.close()
    
    except FileNotFoundError as e:
        print("!!! File not found", e)

def usersInput():
    
    userInput = input("Enter full file path: ")

    userWord = input("Enter the word that you want to be replace (if you want more wordseparate them by |): ")

    userRplWrd = input("Enter the new word: ")
    
    return userInput, userWord, userRplWrd

def seeFullTxt(filePth):
    openFl = open(filePth)
    for line in openFl:
        print(line)
    
    openFl.close()
    
def options(optNum = 0):
    print("To search for a String press 1: ")
    print("To replace strings from text press 2: ")
    
    

if __name__ == "__main__":
    
    a, b, c = usersInput()
    replaceWord(a,b,c)
    seeFullTxt(a)
    
    
        


