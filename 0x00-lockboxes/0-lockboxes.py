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

    unlocked_box = [0]
    for i in range(len(boxes)):
        for j in boxes[i]:
            if j < len(boxes):
                if j in unlocked_box:
                    pass
                else:
                    unlocked_box.append(j)

#    unlocked_box.append(0)

    if len(unlocked_box) == len(boxes):
        return True
    else:
        return False
if __name__ == "__main__":
#   boxes =  [[4, 6], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    boxes = [[1, 4, 5], [2], [5, 2], [3], [4, 1], [3, 5]]
    print(canUnlockAll(boxes))
