#!/usr/bin/python3
""" This module contains a pacscal triangule function """


def pascal_triangle(n):
    """ return the list of interger representation """
    triangle_list = []

    if n >= 1:
        triangle_list.append([1])
    if n >= 2:
        triangle_list.append([1, 1])

    if not n > 2:
        return triangle_list

    for i in range(2, n):
        new_triangle_list = [1]
        previous_triangle_list = triangle_list[i - 1]
        for j in range(0, len(previous_triangle_list) - 1):
            new_triangle_list.append(previous_triangle_list[j] +
                                     previous_triangle_list[j + 1])

        new_triangle_list.append(1)
        triangle_list.append(new_triangle_list)
    return triangle_list
