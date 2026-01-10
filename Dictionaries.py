person = {
    "name": "Alice",
    "age": 25
}
print(person["name"])

person["height"] = 5.7
print(person)

del person["age"]
print(person)

print("age" in person)

for key, value in person.items():
    print(f"{key}: {value}")
    
print(len(person))