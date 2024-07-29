"""
Read an integer value, which is the duration in seconds of a certain event in a factory, and inform it expressed in hours:minutes:seconds.

Input
The input file contains an integer N.

Output
Print the read time in the input file (seconds) converted in hours:minutes:seconds like the following example.
"""

TI = False
while TI != True:
    tid = int(input())
    if tid != 0:
        TI = True

time = int(tid/3600)
tid = tid%3600
minut = int(tid/60)
tid = tid%60
sekund = int(tid/1)
tid = tid%1


print(f"{time}:{minut}:{sekund}")
