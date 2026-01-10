# Arithmetic
a = 10
b = 5
print(a + b)  # Addition
print(a - b)  # Subtraction
print(a * b)  # Multiplication
print(a / b)  # Division
print(a % b)  # Modulo
print(a ** b) # Exponentiation
print(a // b) # Floor Division
# Comparison
print(a == b) # Equal
print(a != b) # Not Equal
print(a > b)  # Greater Than
print(a < b)  # Less Than
print(a >= b) # Greater Than or Equal To
print(a <= b) # Less Than or Equal To
# Logical
x = True
y = False
print(x and y) # Logical AND
print(x or y)  # Logical OR
print(not x)   # Logical NOT
# Bitwise
c = 6  # 110 in binary
d = 3  # 011 in binary
print(c & d)  # Bitwise AND
print(c | d)  # Bitwise OR
print(c ^ d)  # Bitwise XOR
print(~c)     # Bitwise NOT
print(c << 1) # Left Shift
print(c >> 1) # Right Shift
# Assignment
e = 10
e += 5  # e = e + 5
print(e)
e -= 3  # e = e - 3
print(e)
e *= 2  # e = e * 2
print(e)
e /= 4  # e = e / 4
print(e)
e %= 3  # e = e % 3
print(e)
e **= 2 # e = e ** 2
print(e)
e //= 2 # e = e // 2
print(e)
# Membership
my_list = [1, 2, 3, 4, 5]
print(3 in my_list)    # True
print(6 not in my_list) # True
# Identity
f = my_list
g = my_list
print(f is g)      # True
print(f is not g)  # False
h = my_list[:]
print(f is h)      # False
print(f is not h)  # True
print(f == h)      # True
print(f != h)      # False
# Ternary
age = 20
status = "Adult" if age >= 18 else "Minor"
print(status)
# Chained Comparison
num = 15
print(10 < num < 20) # True
print(10 < num <= 15) # True
print(10 <= num < 15) # False
print(10 <= num <= 15) # True
# Operator Precedence
result = 10 + 5 * 2  # Multiplication first
print(result)        # 20
result = (10 + 5) * 2 # Parentheses first
print(result)        # 30
# Augmented Assignment with Bitwise
h = 5  # 101 in binary
h &= 3 # h = h & 3
print(h) # 1 (001 in binary)
h |= 2 # h = h | 2
print(h) # 3 (011 in binary)
h ^= 1 # h = h ^ 1
print(h) # 2 (010 in binary)
h <<= 1 # h = h << 1
print(h) # 4 (100 in binary)
h >>= 1 # h = h >> 1
print(h) # 2 (010 in binary)
# Combining Logical and Comparison
age = 25
income = 50000
is_eligible = (age > 18) and (income > 30000)
print(is_eligible) # True
# Using 'not' with Comparison
is_minor = not (age >= 18)
print(is_minor) # False
# Nested Ternary
score = 85
grade = "A" if score >= 90 else "B" if score >= 80 else "C"
print(grade) # B
# Using 'in' with Strings
text = "Hello, world!"
print("world" in text)    # True
print("Python" not in text) # True
# Combining Membership and Identity
list1 = [1, 2, 3]
list2 = list1
list3 = list1[:]
print(list1 is list2)      # True
print(list1 is not list3)  # True
print(2 in list1)          # True
print(4 not in list1)      # True
# Complex Expressions
a = 5
b = 10
c = 15
result = (a + b) * c / (b - a) ** 2
print(result) # 30.0
# Using all() and any() with Logical Operators
values = [True, False, True]
print(all(values)) # False
print(any(values)) # True
# Combining Multiple Operators
x = 4
y = 2
z = 8
result = (x + y) * (z - y) / (x ** 2 - y ** 2)
print(result) # 3.0
# Using divmod() for Division and Modulo
quotient, remainder = divmod(10, 3)
print(quotient)  # 3
print(remainder) # 1
# Using pow() for Exponentiation
print(pow(2, 3)) # 8
print(pow(2, 3, 3)) # 2 (2^3 % 3)
# Using abs() for Absolute Value
print(abs(-10)) # 10
print(abs(10))  # 10
# Using round() for Rounding
print(round(3.14159, 2)) # 3.14
print(round(3.14159))    # 3
# Using isinstance() for Type Checking
print(isinstance(10, int))    # True
print(isinstance(10.5, float)) # True
print(isinstance("Hello", str)) # True
# Using id() for Identity
x = 10
y = x
print(id(x) == id(y)) # True
y += 1
print(id(x) == id(y)) # False
# Using eval() for Evaluating Expressions
expr = "3 + 5 * 2"
print(eval(expr)) # 13
# Using format() for String Formatting
name = "Alice"
age = 30
print("Name: {}, Age: {}".format(name, age)) # Name: Alice, Age: 30
# Using f-strings for String Interpolation (Python 3.6+)
print(f"Name: {name}, Age: {age}") # Name: Alice, Age: 30
# Using zip() for Combining Iterables
list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
for num, char in zip(list1, list2):
    print(num, char)
# 1 a
# 2 b
# 3 c
# Using map() for Applying Functions
def square(x):
    return x * x