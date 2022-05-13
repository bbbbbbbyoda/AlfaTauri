# 3
# Students room:
# Реализуйте студенческую комнату с помощью ООП:
# Copy:

# print(Steve)
# <name: Steven Schultz, age: 23, major: English>
# print(Johnny)
# <name: Jonathan Rosenberg, age: 24, major: Biology>


class Student:

    def __init__(self, name, age, major):
        self.check_age(age)
        self._name = name
        self._age = age
        self._major = major

    @classmethod
    def check_age(cls, age):
        if type(age) != int:
            raise TypeError("Возраст должен быть целым числом!")
    @property
    def getname(self):
        return self._name

    @property
    def getage(self):
        return self._age

    @property
    def getmajor(self):
        return self._major

    def __str__(self):
        return f'<name: {self._name}, age: {self._age}, major: {self._major} >'


Steve = Student("Steven Schultz", 23, "English")
Johnny = Student("Jonathan Rosenberg", 24, "Biology")
Penny = Student("Penelope Meramveliotakis", 21, "Physics")

print(Penny, Steve, Johnny)
