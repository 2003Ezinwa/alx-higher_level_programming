#!/usr/bin/python3
def islower(c):
    for alpha in range(ord('a'), ord('z') + 1):
        if ord(c) == alpha:
            return True
        else:
            continue
    if ord(c) != alpha:
        return False
