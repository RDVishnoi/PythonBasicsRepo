name = "Alice"    # String
age = 25          # Integer
height = 5.7     # Float
is_student = True # Boolean
print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is Student:", is_student)
# Multiple assignments
x, y, z = 1, 2.5, "Hello"
print("x:", x)
print("y:", y)
print("z:", z)
# Constants (by convention, use uppercase variable names)
PI = 3.14159
GRAVITY = 9.81
print("PI:", PI)
print("Gravity:", GRAVITY)
# Type conversion
age_str = str(age)          # int to str
height_int = int(height)    # float to int
is_student_str = str(is_student) # bool to str
print("Age as string:", age_str)
print("Height as integer:", height_int)
print("Is Student as string:", is_student_str)
# Using type() to check variable types
print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of height:", type(height))
print("Type of is_student:", type(is_student))