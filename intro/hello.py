'''
print("Hello World")
print('Hello World')

pi = 3.14
print(pi)
print(int(pi))


def multipi(i: int):

    print(i * pi)


multipi(10)

print("hello".capitalize())
print("hello".isalpha())

name = "Ann"
print("Hello, {0}".format(name))
print(f"Hello {name}")


isCat = False


if isCat:
    print("Leo is a cat")
else:
    print("Leo is not a cat")

# Ternary statement

print("T Leo is a Cat") if isCat else print("T Leo is not a cat")


num = "None"
if num is not None:
    print("num is truthy")
else:
    print("num is falsy")

age = 18
hasLearningPermit = True


if age >= 18 and hasLearningPermit:
    print("Liza can drive")
else:
    print("Liza cannot drive")

'''
#Lists

marks = [10, 20, 30, 40]

for value in marks:
    print(value)

print(marks[2])


marks.append(50)
print(marks)

digits = []
for x in range(0, 10, 1):
    digits.append(x)
print(digits)

value1 = 2
value2 = 3
print(value1 / value2)

sum_of_digits = 0
for value in digits:
    sum_of_digits = sum_of_digits + value

print(f"The sum is {sum_of_digits}")
average = sum_of_digits / len(digits)
print(f"The average is {average}")

