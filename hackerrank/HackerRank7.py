#!/bin/python3
'''
Task 
Given an array, , of  integers, print 's elements in reverse order as a single line of space-separated numbers.

Sample Input
    4
    1 4 3 2

Sample Output
    2 3 4 1
'''

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    print(*list(reversed(arr)))
