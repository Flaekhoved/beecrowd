# -*- coding: utf-8 -*-

'''
Calculate a car's average consumption being provided the total distance traveled (in Km)
and the spent fuel total (in liters).

Input
The input file contains two values: one integer value X representing the total distance (in Km)
and the second one is a floating point number Y  representing the spent fuel total, with a digit after the decimal point.

Output
Present a value that represents the average consumption of a car with 3 digits after the decimal point,
followed by the message "km/l".

Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
X = float(input())
Y = float(input())

kml = X/Y

print(f"{kml:.3f} km/l")
