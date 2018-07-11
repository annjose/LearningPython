'''
for loops and while loops
'''

'''
names = ["Ann", "Liza", "George"]
for name in names:
    print(f"Name is {name}")
print()

for x in range(5):
    print(f"value of x = {x}")

print()
for x in range(5, 10, 2):
    print(f"value of x = {x}")

print()

for name in names:
    if name == "Liza":
        print("Found Liza")
        break
    print(name)

'''

print("DICTIONARIES")
''' 
Dictionaries
'''


dict = {
    "name": "value1",
    "name": "value2",
    1: "value3",
    None: None,
    None: "value5"
}

'''
print(dict)

print(dict["name"])
print(dict[1])


list_of_dict = [
    {"row1-key1": "row1-value1", "row1-key2": "row1-value2"},
    {"row2-key1": "row2-value1", "row2-key2": "row2-value2"}
]


print(f"list_of_dict = {list_of_dict}")

print(list_of_dict[0]["row1-key2"])

# KeyError example
# #print(f"list_of_dict[0][\"dd\"] = {list_of_dict[0]['dd']}")


print(f"list_of_dict[0][\"dd\"] = {list_of_dict[0].get('dd' 'default value')}")

print(list_of_dict[0].get("dd", "default value"))


print("\nPython's print....")
print(dict)

print("\nLiza's beautiful print...")
print("{", end='')
for key in dict.keys():
    print(f"'{key}' => '{dict[key]}'", end='')

print("}", end='')

print()

'''

family = {
    "father": "Kunjachan",
    "mother": "Alice",
    "children": [
        {
            "father": "Sherry",
            "mother": "Archana",
            "child1": "Joe",
            "child2": "Kunju"
        },
        {
            "father": "George",
            "mother": "Anu",
            "child1": "Liza",
        },
        {
            "father": "Manu",
            "mother": "Ancy",
            "child1": "Manas",
            "child2": "Mili"
        }
    ]
}
print(f"family = {family}")

"I am {Liza}"

print("I am " + family["children"][1]["child1"])
"My brothers are Joe, Kunju and Manas"

print("My brothers are " + family["children"][0]["child1"] + ", " + family["children"][0]["child2"] + ", and " + family["children"][2]["child1"])














