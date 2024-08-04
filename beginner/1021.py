"""
Read a value of floating point with two decimal places.
This represents a monetary value. After this, calculate the smallest possible number of notes and coins on which the value can be decomposed. 
The considered notes are of 100, 50, 20, 10, 5, 2. The possible coins are of 1, 0.50, 0.25, 0.10, 0.05 and 0.01. 
Print the message “NOTAS:” followed by the list of notes and the message “MOEDAS:” followed by the list of coins.
"""

#input value
value = float(input())

#list definition
notas = ["100.00", "50.00", "20.00", "10.00", "5.00", "2.00"]
moedas = ["1", "0.50", "0.25", "0.10", "0.05", "0.01"]

#convert lists to float
notas = [float(n) for n in notas]
moedas = [float(m) for m in moedas]

print("NOTAS:")

#iteration through notes
for note in notas:
    amount = int(value / note) #round down to nearest whole number
    value = value % note #find remaining value and round to 2 decimals
    print(f"{amount} nota(s) de R$ {note:.2f}")
    
print("MOEDAS:")

#iteration through coins

for moeda in moedas:
    amount = int(round(value, 2) / moeda) #round to 2 decimals because of small values
    value = value % moeda #find remaining value and round to 2 decimals
    print(f"{amount} moeda(s) de R$ {moeda:.2f}")
