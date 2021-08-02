# This program is @staticmethod use in python
class Employee:
    no_of_leaves=8
    def __init__(self, aname, asalary, arole):
        self.name=aname
        self.salary=asalary
        self.role=arole
    def printdetails(self):
        return f"Name is {self.name}. salary is {self.salary} and role is {self.role}"
    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves

    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good"+ string)
        return 0

harry=Employee("Harry",4500,"Instructor")
rohan=Employee("Rohan",4600,"Manager")
karan=Employee.from_dash("Karan-400-Student")
rohan.change_leaves(43)
#print(harry.printdetails())
#print(karan.salary,karan.name)
print(karan.printgood(" harry"))