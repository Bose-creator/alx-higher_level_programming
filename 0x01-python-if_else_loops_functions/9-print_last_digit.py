#!/usr/bin/python3
def print_last_digit(number):
    """
    Print the last digit of a number.
    Args:
    number (int): The number to get the last digit from
    Returns:
    int: The last digit of the number
    """
    last_digit = abs(number) % 10
    print(last_digit)
    return last_digit
print_last_digit(1234)
print_last_digit(-1234)
