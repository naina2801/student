class Professor:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print("Name:{} Age:{}".format(self.name,self.age))
class Student(Professor):
    def __init__(self, name, age,section):
        super().__init__(name, age)
        self.section = section
    def displayStudent(self):
        print("Student name : {} age : {} Section : {}".format(self.name,self.age,self.section))

per = Professor("Star Boy", 21)
per.display()
std = Student("Mappy",12,"A")
std.displayStudent()

