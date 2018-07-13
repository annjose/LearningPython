
students = []
def add_student(name, age=15):
    student = {
        "name": name,
        "age": age
    }
    students.append(student)
    print(f"Added new student with name '{name}' and age '{age}'")

def my_print(name, age, *args):
    print("name =", name, "age =", age)
    print(args)


my_print("Liza", 14, "a", 12, "bd")

name = "ann catherine"
print(name.title())

student_name = input("Enter student's name: ")
student_age = input("Enter student's age: ")
add_student(student_name, student_age)

print(students)

print("------------------")


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


