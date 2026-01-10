print("Hello, World!")
text = "Hello, world!"
print("world" in text)  # True
print("Python" not in text) # True
print("world" in "Hello, world!")  # True
print("Python" not in "Hello, world!") # True
print("Hello" in "Hello, world!")  # True
print("world!" in "Hello, world!")  # True
print("hello" in "Hello, world!")  # False (case-sensitive)
print("WORLD" in "Hello, world!")  # False (case-sensitive)
print(" " in "Hello, world!")  # True (space character)
print("," in "Hello, world!")  # True (comma character)
print("!" in "Hello, world!")  # True (exclamation mark)
print("o" in "Hello, world!")  # True (letter 'o')
print("z" in "Hello, world!")  # False (letter 'z')
print("Hello, world!" in "Hello, world!")  # True (entire string)
print("Hello, world!!" in "Hello, world!")  # False (extra character)
print("" in "Hello, world!")  # True (empty string is always found)
print("Hello, world!" not in "Hello, world!")  # False (entire string)
print("hello" not in "Hello, world!")  # True (case-sensitive)
print("WORLD" not in "Hello, world!")  # True (case-sensitive)
print(" " not in "Hello, world!")  # False (space character)
print("," not in "Hello, world!")  # False (comma character)
print("!" not in "Hello, world!")  # False (exclamation mark)
print("o" not in "Hello, world!")  # False (letter 'o')
print("z" not in "Hello, world!")  # True (letter 'z')
print("" not in "Hello, world!")  # False (empty string is always found)
print("Hello" not in "Hello, world!")  # False (substring)
print("world!" not in "Hello, world!")  # False (substring)
