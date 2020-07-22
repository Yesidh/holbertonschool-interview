#!/usr/bin/python3
"""
=================================
only canUnlockAll function inside
=================================
"""


def canUnlockAll(boxes):
    """
    function for check if all boxes can be open
    into a list, return True if all can be open
    and False else
    """

    unlocked_box = []
    for i in range(len(boxes)):
        for j in range(len(boxes[i])):
            if boxes[i][j] < len(boxes):
                if boxes[i][j] in unlocked_box:
                    pass
                else:
                    unlocked_box.append(boxes[i][j])
        if len(boxes[i]) == 0:
            unlocked_box.append(0)

    if len(unlocked_box) == len(boxes):
        return True
    else:
        return False
