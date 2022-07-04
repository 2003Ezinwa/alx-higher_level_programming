#!/usr/bin/python3


def max_integer(my_list=[]):
    if my_list:
        max = my_list[0]
        for a in my_list:
            if a > max:
                max = a
        return max
    return None
