fruits = ["apple", "banana", "cherry"]
print(fruits[0])  # apple

fruits.append("orange")
print(fruits)
# ['apple', 'banana', 'cherry', 'orange']

fruits.remove("banana")
print(fruits)  # ['apple', 'cherry', 'orange']

print(len(fruits))  # 3

fruits.sort()
print(fruits)  # ['apple', 'cherry', 'orange']

fruits.reverse()
print(fruits)  # ['orange', 'cherry', 'apple']

for fruit in fruits:
    print(fruit)
# orange
# cherry
# apple