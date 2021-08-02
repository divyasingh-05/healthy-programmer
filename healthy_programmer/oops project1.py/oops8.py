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
class Player:
    no_of_game=4
    def __init__(self,name,game):
        self.name=name
        self.game=game

    def printdetail(self):
        return f"Name is {self.name}. Game is {self.game}."
class Coolprogrmmer(Employee,Player):
    pass

harry=Employee("Harry",4500,"Instructor")
rohan=Employee("Rohan",4600,"Manager")
karan=Employee.from_dash("Karan-400-Student")
rohan.change_leaves(43)
sohan=Player("Sohan","[Cricket]")
moti=Coolprogrmmer("Moti",80000,"Coolprogrammer")
fun=moti.printdetails()
print(fun)