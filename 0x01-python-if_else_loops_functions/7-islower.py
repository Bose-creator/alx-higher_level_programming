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

# Example usage:
print(islower('a'))  # Should return True
print(islower('z'))  # Should return True
print(islower('A'))  # Should return False
print(islower('Z'))  # Should return False
print(islower('1'))  # Should return False
print(islower('?'))  # Should return False
