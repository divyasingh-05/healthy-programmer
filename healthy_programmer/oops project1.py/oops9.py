class Employee:
    no_of_leaves=8
    _protected=12
    __private=15

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

emp=Employee("harry",343,"programmer")
print(emp._protected)
print(emp._Employee__private)