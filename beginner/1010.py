# -*- coding: utf-8 -*-

'''
In this problem, the task is to read a code of a product 1, the number of units of product 1, the price for one unit of product 1,
the code of a product 2, the number of units of product 2 and the price for one unit of product 2. After this, calculate and show the amount to be paid.

Input
The input file contains two lines of data. In each line there will be 3 values:
two integers and a floating value with 2 digits after the decimal point.

Output
The output file must be a message like the following example where "Valor a pagar" means Value to Pay.
Remember the space after ":" and after "R$" symbol. The value must be presented with 2 digits after the point.

Escreva a sua solução aqui
Code your solution here
Escriba su solución aquí
'''
kode1, antal1, pris1 = input().split()
kode2, antal2, pris2 = input().split()

antal1 = int(antal1)
antal2 = int(antal2)
pris1 = float(pris1)
pris2 = float(pris2)

samlet = (antal1 * pris1) + (antal2 * pris2)

print(f"VALOR A PAGAR: R$ {samlet:.2f}")
