#!/bin/python

import sys
import re

n, m = raw_input().strip().split(' ')
n, m = [int(n), int(m)]
matrix = []
matrix_i = 0
for matrix_i in xrange(n):
    matrix_t = str(raw_input())
    matrix.append(matrix_t)

# Decoding matrix script - reading column wise values
scrpt = ''

for j in range(m):
    for i in range(n):
        try:
            scrpt += str(matrix[i][j])
        except IndexError:
            scrpt += ' '

# print scrpt
print re.sub(r'(?<=[a-zA-Z0-9])([!@#$%& ])+(?=[a-zA-Z0-9])', ' ', scrpt)
