import types
types.ClassType

import sys
print sys.version

# Create new class
class Employee:
    'Common base class for all employees'
    empCount = 0

    # Constructor
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    # Destructor
    def __del__(self):
        class_name = self.__class__.__name__
        print class_name, "destroyed"

    def displayCount(self):
        print "Total Employee %d" % Employee.empCount

    def displayEmployee(self):
        print "Name : ", self.name, ", Salary: ", self.salary


"This would create first object of Employee class"
emp1 = Employee("Zara", 2000)
"This would create second object of Employee class"
emp2 = Employee("Manni", 5000)

emp1.displayEmployee()
emp2.displayEmployee()
print "Total Employee %d" % Employee.empCount

print "Employee.__doc__
