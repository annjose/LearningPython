
## simple function


def say_hello(name):
    print(f"Hello {name}")


say_hello("Ann")  # prints "Hello Ann"


def add_these_two(num1, num2):
    return num1 + num2


sum1 = add_these_two(num1=10, num2=20)  # Named arguments
print(f"Sum of 10 and 20 = {sum1}")

sum2 = add_these_two(10, 20)
print(f"Sum of 10 and 20 = {sum2}")


# more complex function
students = []


def add_student(name, age=15):
    student = {
        "name": name,
        "age": age
    }
    students.append(student)
    print(f"Added new student with name '{name}' and age '{age}'")


# print(f"name = {name}")  # function's argument "name" is not available outside the function scope


def get_student_age(name):
    age = -1
    for student in students:
        if student["name"] == name:
            age = student["age"]
            break

    return age

add_student("Mark", 14)
add_student("Liza", 15)
add_student("DefaultAge")  # default arguments
print(students)

# functions that don't return a value will print "None"
result = add_student("aa", 10)
print(f"result = {result}")

print(get_student_age("Mark"))   # prints 14
print(get_student_age("Donno"))  # prints -1

print("a", 12, "bd")


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

