# Clases

class Programmer:

    def __init__(self, name: str, age: int, language: list):
        self.name = name
        self.age = age
        self.language = language


    def print(self):
        print(f"Name: {self.name}, Age: {self.age}, Language: {self.language}")

my_programmer = Programmer("Juan", 20, ["Python", "Java", "C++"])

my_programmer.print()
