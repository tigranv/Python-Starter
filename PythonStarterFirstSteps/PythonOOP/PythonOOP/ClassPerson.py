
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def print_info(self):
        print(self.name, "is", self.age)

john = Person("john", 22)

lucy = Person("lucy", 23)


Person.print_info(john)
Person.print_info(lucy)

john.print_info()
lucy.print_info()