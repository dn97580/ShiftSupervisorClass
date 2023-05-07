# Project #1: ShiftSupervisor Class
# In a particular factory, a shift supervisor is a salaried employee who supervises a shift.
# In addition to a salary, the shift supervisor earns a yearly bonus when his or her shift meets
# production goals. Write a ShiftSupervisor class that is a subclass of the Employee class you
# created in Programming Exercise 1. The ShiftSupervisor class should keep a data attribute for 
# the annual salary, and a data attribute for the annual production bonus that a shift supervisor 
# has earned. Demonstrate the class by writing a program that uses a ShiftSupervisor object    

class Employee:
    def __init__(self, name, employee_number):
        self.name = name
        self.employee_number = employee_number
        
    def set_name(self, name):
        self.name = name

    def set_employee_number(self, employee_number):
        self.employee_number = employee_number

    def get_employee_number(self):
        return self.employee_number

    def get_name(self):
        return self.name

class ShiftSupervisor(Employee):
    def __init__(self, name, employee_number, annual_salary, annual_bonus):
        super().__init__(name, employee_number)
        self.annual_salary = annual_salary
        self.annual_bonus = annual_bonus

# create a ShiftSupervisor object
supervisor = ShiftSupervisor("John Doe", 12345, 50000, 10000)

# print the object's attributes
print(supervisor.name)
print(supervisor.employee_number)
print(supervisor.annual_salary)
print(supervisor.annual_bonus)

print()
name1 = input('Enter the name of supervisor:  ')
employee_number1 = input('Enter employer number:  ')
supervisor.set_name(name1)
supervisor.set_employee_number(employee_number1)
print(supervisor.get_name())
print(supervisor.get_employee_number())
#print(supervisor.annual_salary)
#print(supervisor.annual_bonus)
