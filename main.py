students_score = {"Thomas": 57, "James": 80, "Jane": 95, "Lucas": 65}

# Do not change the code above ☝️
#################################################################

# TODO 1: Create an empty dictionary, students_grade

# TODO 2: Add each student name from students_score dictionary as the key
#         and the value is the grade of the student

students_grade = {}

for i in students_score:
    value = students_score[i]
    if value >= 80:
        students_grade[i] = "A"
    elif value >= 60:
        students_grade[i] = "B"
    elif value >= 55:
        students_grade[i] = "C"
    elif value >= 50:
        students_grade[i] = "D"
    else:
        students_grade[i] = "F"
#################################################################
# Do not change the code below
print(students_grade)
