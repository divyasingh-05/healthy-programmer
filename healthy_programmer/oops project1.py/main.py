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
harry=Employee("Harry",4500,"Instructor")
rohan=Employee("Rohan",4600,"Manager")
rohan.change_leaves(43)
print(harry.printdetails())
print(harry.no_of_leaves)
