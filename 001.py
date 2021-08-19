#!/bin/python3

import math
import os
import random
import re
import sys

# Python If-Else
"""
Task
Given an integer, , perform the following conditional actions:

If  is odd, print Weird
If  is even and in the inclusive range of  to , print Not Weird
If  is even and in the inclusive range of  to , print Weird
If  is even and greater than , print Not Weird
"""

if __name__ == '__main__':
    n = int(input().strip())
    resto = n % 2
    print(resto)

    if not(100 < n >= 1):
        if resto != 0:
            print("Weird")
        elif resto == 0 and 5 >= n >= 2:
            print("Not Weird")
        elif resto == 0 and 20 >= n >= 6:
            print("Weird")
        elif n >= 20:
            print("Not Weird")
    else:
        exit()