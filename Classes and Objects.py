class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hi, I am {self.name} and I am {self.age} years old.")

person1 = Person("Alice", 25)
person1.greet()
person2 = Person("Bob", 30)
person2.greet()