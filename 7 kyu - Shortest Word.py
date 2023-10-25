"""
Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
"""


def find_short(s):  
    wrd =  min(s.split(), key=len)
    return len(wrd)