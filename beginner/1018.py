# -*- coding: utf-8 -*-
"""
In this problem you have to read an integer value and calculate the smallest possible number of banknotes in which the value may be decomposed. 
The possible banknotes are 100, 50, 20, 10, 5, 2 and 1. Print the read value and the list of banknotes.

Input
The input file contains an integer value N (0 < N < 1000000).

Output
Print the read number and the minimum quantity of each necessary banknotes in Portuguese language, as the given example. 
Do not forget to print the end of line after each line, otherwise you will receive “Presentation Error”.
"""
'''
Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
doll = False
while doll != True:
    dollar = int(input())
    if dollar > 0 and dollar < 1000000:
        doll = True

print(dollar)

hundrede = int(dollar/100)
dollar = dollar%100
halvtreds = int(dollar/50)
dollar = dollar%50
tyve = int(dollar/20)
dollar = dollar%20
ti = int(dollar/10)
dollar = dollar%10
fem = int(dollar/5)
dollar = dollar%5
to = int(dollar/2)
dollar = dollar%2
en = int(dollar/1)
dollar = dollar%1

print(hundrede, "nota(s) de R$ 100,00")
print(halvtreds, "nota(s) de R$ 50,00")
print(tyve, "nota(s) de R$ 20,00")
print(ti, "nota(s) de R$ 10,00")
print(fem, "nota(s) de R$ 5,00")
print(to, "nota(s) de R$ 2,00")
print(en, "nota(s) de R$ 1,00")
