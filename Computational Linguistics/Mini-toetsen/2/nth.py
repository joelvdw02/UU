# -*- coding: utf-8 -*-
def nth_char(n, string):
    """
    :param n: int: which character to return (0-indexed)
    :param string: str the string to return a character from
    :return str: the nth character of string, or None if there is no such character
    """
    if len(string) > n:     
        return string[n]
    elif len(string) <= n:
        return "None"
        
	
def nth_word(n, string):
    """
    splits string into words on whitespace and returns the nth word
    :param n: int: which word to return (0-indexed)
    :param string: str the string to return a character from
    :return str: the nth word of string, or None if there is no such word
    """
    if len(string.split()) > n:
        return string.split()[n]
    else:
        return "None"


def nth_of_mth(n, m, string):
    """
    Prints "Character n of word m is c" where c is the nth character of the mth word of string
    :param n : int : which character to print
    :param m : word: which word to print a character from
    :param string: str : the string to print from
    """
    if len(string.split()) > m:
        word = string.split()[m]
        if len(word) > n:
            letter = word[n]
            antwoord = "Character " + str(n) + " of word " + str(m) + " is " + str(letter) + "."
            return antwoord
        else:
            print("Oops!")
    elif len(string.split()) <= m:
        print("Oops!")
     
