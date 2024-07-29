"""
Read an integer value corresponding to a person's age (in days) and print it in years, months and days, followed by its respective message “ano(s)”, “mes(es)”, “dia(s)”.

Note: only to facilitate the calculation, consider the whole year with 365 days and 30 days every month. 
In the cases of test there will never be a situation that allows 12 months and some days, like 360, 363 or 364. 
This is just an exercise for the purpose of testing simple mathematical reasoning.

Input
The input file contains 1 integer value.

Output
Print the output, like the following example.
"""
ageInDays = False
while ageInDays != True:
    age = int(input())
    if age != 0:
        ageInDays = True

year = int(age/365)
age = age%365
month = int(age/30)
age = age%30
days = int(age/1)
age = age%1




print(year, "ano(s)")
print(month, "mes(es)")
print(days, "dia(s)")
