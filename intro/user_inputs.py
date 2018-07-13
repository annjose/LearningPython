
students = []


def ask_user_input():
    return input("Do you want to add a student? Answer yes or no: ")


add_student = ask_user_input()

while add_student.lower() == "yes" or add_student.lower() == "y":

    # ask the user for student name and age
    student_name = input("Enter student name: ")
    student_age = input("Enter student age: ")

    student = {
        "name": student_name.title(),
        "age": student_age
    }
    students.append(student)

    add_student = ask_user_input()

print("Students ....\n", students)


