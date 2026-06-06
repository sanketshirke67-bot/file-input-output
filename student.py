student = []

with open ("student.csv") as file:
    for line in file :
        name, house =line.rstrip().split(",")
        student = {"name": name, "house": house}
        student.append(student)


def get_name(student):
    return student["name"]

for student in sorted(student):
    print(f"{student['name']} is in {student['house']}")
