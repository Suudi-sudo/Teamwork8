# question 2

class Department:
    def __init__(self, department):
        self.department = department
        self.employees = []
    def adding_employee(self, employee):
        self.employees.append(employee)
        employee.department = self
    def list_employees(self):
        print(f"employees in {self.department}:")
        for employee in self.employees:
            print(f"Name: {employee.name}", f"ID:{employee.id}")

class Employee:
    def __init__(self, name, id):
        self.name = name
        self.id = id
        self.department = None
    def transfer(self, new_department):
        self.department.employees.remove(self)
        new_department.adding_employee(self)
#  creating department
dep1 = Department("frondend dev")
dep2 = Department("backend dev")
# creating employee
emp1 = Employee("Elvis", 48)
emp2 = Employee("Peter", 58)
emp3 = Employee("suudi", 68)
emp4 = Employee("Rose", 78)
# adding employee
dep1.adding_employee(emp1)
dep2.adding_employee(emp2)
dep1.adding_employee(emp3)
dep1.adding_employee(emp4)
# listing
dep1.list_employees()
dep2.list_employees()

emp1.transfer(dep2)

dep1.list_employees()
dep2.list_employees()