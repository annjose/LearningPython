
file_name = "students.txt"


def clear_file_contents():
    try:
        f = open(file_name, "w")
        f.close()
    except Exception:
        print("Could not open file in Write mode")


def read_student_names_from_file():
    try:
        f = open(file_name, "r")
        # print("File contents:", f.readlines())
        # lines = f.readlines()
        lines = my_readlines_2(f)

        print("inside read_student_names_from_file(): all lines: ", lines)
        for line in lines:
            print("inside read_student_names_from_file() for loop: line = ", line)

        f.close()

    except Exception:
        print("Could not open file in Read mode")


def my_readlines_1(file):
    lines = []

    for line in file:
        lines.append(line)

    return lines


def my_readlines_2(file):

    for line in file.readlines():
        print("\t inside my_readlines_2() for loop: line = ", line)
        yield line


def save_student_name_to_file(student_name):
    try:
        f = open(file_name, "a")
        f.write(student_name + "\n")
        f.close()

    except Exception:
        print("Could not open file in Append mode")


# clear_file_contents()


read_student_names_from_file()

'''
student_name = input("Enter you student name: ")
save_student_name_to_file(student_name)
print(f"Saved new student '{student_name}' to {file_name}")

read_student_names_from_file()
'''