
#!/bin/python3

import math
import os
import random
import re
import sys


def diagonalDifference(arr, n):
    # Write your code here
    rtl = []
    ltr = []
    row = n
    col = n
    for i in range(len(arr[0])):
        for j in range(len(arr[1])):
            if i == j:
                ltr.append(arr[i][j])
            row -= 1
            col -= 1

    for i in range(len(arr)):
        for j in range(len(arr) - 1, -1, -1):
            print(i, j)

    print(ltr, rtl)


print(diagonalDifference(
    [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]], 4))
