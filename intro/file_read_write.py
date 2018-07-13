
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
        print("File contents:", f.readlines())
        f.close()

    except Exception:
        print("Could not open file in Read mode")


def save_student_name_to_file(student_name):
    try:
        f = open(file_name, "a")
        f.write(student_name + "\n")
        f.close()

    except Exception:
        print("Could not open file in Append mode")


# clear_file_contents()

read_student_names_from_file()

student_name = input("Enter you student name: ")
save_student_name_to_file(student_name)
print(f"Saved new student '{student_name}' to {file_name}")

read_student_names_from_file()
