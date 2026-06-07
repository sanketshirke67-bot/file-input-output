# Write a name
name = input("What's your name? ")
with open("names.txt", "a") as file:
    file.write(name + "\n")

# Then read all names
with open("names.txt", "r") as file:
    lines = file.readlines()
    for line in lines:
        print("hello,", line.strip())