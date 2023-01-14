class Employee:
    no_of_leaves = 9
    def __init__(self,aName,aSalary,aRole):
        self.name=aName
        self.salary=aSalary
        self.role=aRole


    def Printdetails(self):
        return f"Name is {self.name}, Salary is {self.salary}, role is {self.role}"


shubham =Employee("Shubham",10000000,"Captain")  # always goes to init

print(shubham.name,shubham.salary,shubham.role)

# shubh = Employee()
# kumar = Employee()

# shubh.name = "SHUB"
# shubh.salary = 555555555
# shubh.role = "Captain"
#
# kumar.name = "ku"
# kumar.salary = 55555
# kumar.role = "leutinent"
# print(shubh.name)
#
# print(kumar.__dict__)
#
# kumar.no_of_leaves = 10
# print(kumar.__dict__)

# print(shubh.Printdetails())

