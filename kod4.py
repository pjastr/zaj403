class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def welcome(self):
        print("Welcome", self.firstname, self.lastname, "to the class of", self.graduationyear)


s1 = Student("Jan","Kowalski", 2020)
s1.printname()
s1.welcome()
s2 = Student("Jan","Kowalski", 2020)
print(s1 == s2)
s3 = s1
print(s1 == s3)
