#!/usr/bin/python3


def print_matrix_integer(matrix=[[]]):
    for lists in matrix:
        print(" ".join("{:d}".format(a) for a in lists))
