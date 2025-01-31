# -*- coding: utf-8 -*-

'''

Read the four values corresponding to the x and y axes of two points in the plane,
p1 (x1, y1) and p2 (x2, y2)
and calculate the distance between them, showing four decimal places, according to the formula:

Distance = Kvadratroden af: (x2-x1)^2 + (y2-y1)^2

Input
The input file contains two lines of data.
The first one contains two double values:
x1 y1 and the second one also contains two double values with one digit after the decimal point: x2 y2.

Output
Calculate and print the distance value using the provided formula, with 4 decimal places.
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
import math
x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

tal = ((x2 - x1)**2) + ((y2 - y1)**2)
kvadratrod = math.sqrt(tal)

print(f"{kvadratrod:.4f}")

