# -*- coding: utf-8 -*-

'''

Make a program that reads 3 integer values and present the greatest one followed by the message "eh o maior".
Use the following formula:

MaiorAB = (a+b+abs(a-b))/2

Input
The input file contains 3 integer values.

Output
Print the greatest of these three values followed by a space and the message “eh o maior”.
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
A,B,C = map(int, input().split())

størst = max(A, B, C)

print(f"{størst} eh o maior")
