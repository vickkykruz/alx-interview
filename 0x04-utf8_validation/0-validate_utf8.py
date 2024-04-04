#!/usr/bin/env python3
""" This is a module that write a method that determines if a given
data set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    Args:
    - data: a list of integers representing bytes

    Returns:
    - True if data is a valid UTF-8 encoding, else False
    """
    num_bytes_to_follow = 0

    bytes1 = 1 << 7
    bytes2 = 1 << 6

    for i in data:
        byte = 1 << 7
        if num_bytes_to_follow == 0:

            while byte & i:
                num_bytes_to_follow += 1
                byte = byte >> 1
            if num_bytes_to_follow == 0:
                continue
            if num_bytes_to_follow == 1 or num_bytes_to_follow > 4:
                return False
        else:
            if not (i & bytes1 and not (i & bytes2)):
                return False
        num_bytes_to_follow -= 1

    return num_bytes_to_follow == 0
