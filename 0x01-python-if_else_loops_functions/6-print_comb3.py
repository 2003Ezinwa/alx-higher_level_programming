#!/usr/bin/python3
for a in range(0, 9):
    for b in range(1, 10):
        if a == 8 and b == 9:
            print("{}{}".format(a, b))
        else:
            if a < b:
                print("{}{}, ".format(a, b), end="")
            else:
                continue
