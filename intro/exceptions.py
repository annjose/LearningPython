student = {
    "name": "Mark"
}

try:
    print(student["last_name"])
except KeyError:
    print("Error finding key")