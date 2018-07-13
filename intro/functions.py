
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

print("-------------Return statements----------------")
def my_function():
    print("Inside my_function(). Before return. This line will be printed")
    return

    print("Inside my_function(). After return. This line won't be printed")

my_function()
print("-----------------------------")

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

### Nested Functions
print("------------Nested Functions START-----------------")

def double_and_print(number):

    my_number = number

    def double(my_number):
        return my_number * 2

    result = double(my_number)

    print(f"double of {number} = {result}")

double_and_print(10)
double_and_print(20)

print("------------Nested Functions END-----------------")

## Lambda Functions - anonymous functions
print("-----------Lambda Functions START------------------")
def double1(num):
    return num * 2

double2 = lambda num: num * 2

print("double1 - regular function =", double1(3))
print("double2 - lambda function =", double2(3))

print("-----------Lambda Functions END------------------")

### Function Scoping

def foo():
    print("foo")
    bar()

    # call foobar which is defined below foo() and bar()
    foobar()


def bar():
    print("bar")

# this won't work because foobar() which is defined BELOW the call-site of foo()
# foo()


def foobar():
    print("foobar")

# this will work because at the call-site of foo(), foobar() is already defined
foo()