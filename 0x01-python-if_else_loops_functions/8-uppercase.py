#!/usr/bin/python3
def uppercase(str):
    """
    Print a string in uppercase followed by a new line.
    Args:
    str (str): The string to be converted to uppercase
    """
    for char in str:
        if 'a' <= char <= 'z':
            print(chr(ord(char) - 32), end="")
        else:
            print(char, end="")
    print()
uppercase("Hello, World!")
