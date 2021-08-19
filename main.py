#!/bin/python3

import math
import os
import random
import re
import sys

if __name__ == '__main__':



    # if __name__ == '__main__':
    #     n = int(input())
    #     i = 1
    #     numbers = list(range(0, n))
    #     if not (20 < n >= 1):
    #         for i in range(len(numbers)):
    #             print(numbers[i] * numbers[i])
    #     else:
    #         exit()

    # Leap year
    # def is_leap(year):
    #     leap = False
    #     divideby4 = year % 4
    #     divideby100 = year % 100
    #     divideby400 = year % 400
    #
    #     if 1900 <= year <= 10 ** 5:
    #         if divideby4 == 0 and not (divideby100 == 0):
    #             leap = True
    #         elif divideby400 == 0:
    #             leap = True
    #         else:
    #             leap = False
    #     else:
    #         print("exit")
    #         exit()
    #
    #     return leap
    #
    # year = int(input())
    # print(is_leap(year))

    # uso do range em python para lista strings
    # if __name__ == '__main__':
    #     n = int(input())
    #     i = 1
    #     if 1 <= n <= 150:
    #         print(range(1, int(n) + 1), sep='')
    #         # sep é o separador da lista
    #     else:
    #         exit()

    # if __name__ == '__main__':
    #     total = []
    #     for _ in range(int(input())):
    #         name = input()
    #         score = float(input())
    #         name_score = list((score, name))
    #         total.append(name_score)
    # # Ordenando a lista do menor pro maior
    # total.sort()
    # # Adicionando a primeira nota a lista qual vai ser a menor
    # primeiranota = total[0][0]
    #
    # # Loop through the list by excluding first item in the list and find the second lowest
    # for i in range(1, len(total)):
    #     if primeiranota < total[i][0]:
    #         primeiranota = total[i][0]
    #         break
    #
    #     # Loop through the list and print names based on the second lowest score
    # for i in range(1, len(total)):
    #     if total[i][0] == primeiranota:
    #         print(total[i][1])

    # Basic DataTypes - Finding the percentage
    # if __name__ == '__main__':
    #     n = int(input())
    #     student_marks = {}
    #     avgDict = {}
    #     for _ in range(n):
    #         name, *line = input().split()
    #         scores = list(map(float, line))
    #         student_marks[name] = scores
    #     query_name = input()
    #     for k, v in student_marks.items():
    #         # v is the list of grades for student k
    #         avgDict[k] = sum(v) / float(len(v))
    #     print("%.2f" % avgDict[query_name])

    # Python Functionals - Reduce Funcion
