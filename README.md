# file-input-output

start code 

name = input("What's your name? ")
with open("names.txt", "a") as file:
    file.write(name + "\n")

first changes 

with open("names.txt", "r") as file:
    lines = file.readlines()

for line in lines:
    print("hello,", line) 

new things are "r" is for read their is code 
    lines = file.readlines()    
    
