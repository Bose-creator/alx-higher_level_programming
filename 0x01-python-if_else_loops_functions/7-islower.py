#!/usr/bin/python3
def islower(c):
    """
    Check if a character is lowercase.
    Args:
    c (str): A single character
    Returns:
    bool: True if c is lowercase, False otherwise
    """
    return ord('a') <= ord(c) <= ord('z')
print(islower('a'))
print(islower('z'))
print(islower('A'))
print(islower('Z'))
print(islower('1'))
print(islower('?'))
