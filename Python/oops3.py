class Employee:
    no_of_leaves = 9
    def __init__(self,aName,aSalary,aRole):
        self.name=aName
        self.salary=aSalary
        self.role=aRole


    def Printdetails(self):
        return f"Name is {self.name}, Salary is {self.salary}, role is {self.role}"

    @classmethod
    def Change_leaves(cls,new_leaves):
        cls.no_of_leaves = new_leaves




shubham = Employee("Shubham", 100000000, "Captain")
saum = Employee("saumya",1000000,"lieutenant")

saum.Change_leaves(16)
shubham.Change_leaves(15)

print(saum.no_of_leaves)
print(shubham.no_of_leaves)