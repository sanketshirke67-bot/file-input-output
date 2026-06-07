# File Input/Output Project
 

today learn "r" readlines function and  rstrip  and /n to print input on next

code #2
with open("names.txt", "r") as file:
    for line in file:
        print("hello,", line.rstrip())

code #3

i mistakenly put [name] instead {name}

new things 
names =[]

with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names):
    print(f"hello, {name}")


code#4
with open("names.txt") as file:
    for line in sorted(file):
        print("hello", line.rstrip())



code #5

names =[]

reverse=
with open("names.txt") as file:
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"hello, {name}")