class Employee:
    no_of_leaves=8
    def __init__(self, aname, asalary, arole):
        self.name=aname
        self.salary=asalary
        self.role=arole
    def printdetails(self):
        return f"Name is {self.name}. Salary is {self.salary} and role is {self.role}"
    @classmethod
    def change_leaves(cls,newleaves):
        cls.no_of_leaves=newleaves

    @classmethod
    def from_dash(cls,string):
        return cls(*string.split("-"))

    @staticmethod
    def printgood(string):
        print("This is good"+ string)
class Programmer(Employee):
    no_of_holiday =56
    def __init__(self,aname,asalary,arole,languages):
        self.name=aname
        self.salary=asalary
        self.role=arole
        self.languages=languages
    def priniprog(self):
        return f"Programmer's Name is {self.name}. Salary is {self.salary} and role is {self.role}.The languages are{self.languages}"

harry=Employee("Harry",4500,"Instructor")
rohan=Employee("Rohan",4600,"Manager")
karan=Employee.from_dash("Karan-400-Student")

ayush=Programmer("Ayush",6000,"Programmer","[Python, C++]")
raja=Programmer("Ayush",6000,"Programmer","[Python]")

print(ayush.priniprog())
print(ayush.no_of_holiday)