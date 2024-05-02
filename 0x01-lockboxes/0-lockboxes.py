#!/usr/bin/python3
"""
Module that defines the canUnlockAll function
"""


def canUnlockAll(boxes):
    """
    Checks if all boxes can be opened
    """
    n = len(boxes)
    keys = [0]
    for key in keys:
        for boxKey in boxes[key]:
            if boxKey not in keys and boxKey < n:
                keys.append(boxKey)
    if len(keys) == n:
        return True
    return False
