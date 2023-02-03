"""Simple, given a string of words, return the length of the shortest word(s).

String will never be empty and you do not need to account for different data types.
"""


def find_short(s):
    lengths = [len(i) for i in s.split()]
    lengths.sort()
    return lengths[0]
