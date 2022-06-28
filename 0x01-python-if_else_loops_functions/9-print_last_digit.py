#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        number = -number
    lastdig = number % 10
    print(lastdig, end='')
    return(number)
