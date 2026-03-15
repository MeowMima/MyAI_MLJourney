#Method - A fn assosciated with a Class
#Class - A "Blueprint"/"Template" to create objects
#Object - An object can be understood as the actual 'house' made of that blueprint/class i.e. an instance of a class
#NOTE - Each new object you create acquires a new memory space

#Let's Get Started!

class Employee:       #Created class Employee
    #pass              #'pass' keyword is used when you don't really have to pass on any info immediately to the func/method/class
    num_of_emps = 0
    raise_amt = 1.04

    def __init__(self, first, last, pay):        #this ia func defined under a class i.e. a method to create a constructor of the class whereas, 'self' keyword is used to denote 'instance' of the class which will be created as the first argument passed in the method
        self.first = first                       #'Attributes' of the class 'Employee'
        self.last = last
        self.pay = pay

    #let us create an 'email updation' method that can still be called as an attribute
    #self.email = first + "." + last + "@company.com"
    @property                              #using this simple "decorator"
    def email(self):                             
        return "{}.{}@company.com".format(self.first, self.last)
    
    @property                                     #this will behave like 'getter' already
    def fullName(self):                           #a method to print the full name of the employee where 'self' i.e. 'object' is the only argument 'passed' 
        return "{} {}".format(self.first, self.last)
    
    @fullName.setter
    def fullName(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    @fullName.deleter
    def fullName(self):
        print("Deleted!")
        self.first = None
        self.last = None
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)

# '*args' & '**kwargs'
#__________________________________________________
# 'Positional Argument - *args' - take as many arguments, unpack the elements in Tuple(immutable) form
    def total_pay(self, *bonuses):   #an employee can get many bonuses - hence here *args is *bonuses
        return 'Total payment: {} '.format(self.pay + sum(bonuses))    
# 'Keyword Argument - **kwargs' - take as many keyword arguments, in dictionary form, key:item pair - look at Developer class for ex

    def __repr___(self):    #unambiguous reprsn of obj
        return '{} {} {}'.format(self.first, self.last, self.pay)

    def __str__(self):
        return '{} {} {}'.format(self.fullName(), self.email, self.pay)

#CLASS METHODS
#With 'Class Methods' we work with classes(class variable precisely) instead of their instances i.e. -
    @classmethod                                 #decorator
    def set_raise_amt(cls, amt):                 #as instance is denoted by parameter "self", in class methods, an instance(i.e. the class itself) is denoted by "cls"(sincle 'class' keyword is already reserved)
        cls.raise_amt = amt

#using class methods as alternative constructors    
    @classmethod
    def from_string(cls, emp_str):            #hence class methods can be used as alternative constructors
        first, last, pay = emp_str.split('-')
        return cls(first, last, pay)
    
    #STATIC METHODS - do not operate on any instance/class
    @staticmethod
    def is_work_day(day):         #i.e. actually works like a regular function
        if day.weekday == 5 or day.weekday == 6:
            return False
        else:
            return True
        
emp_1 = Employee("Test", "User", 1000)    #emp_1 is the 'object' of the 'class' Employee
        
"""
import datetime           
my_date = datetime.date(2026, 2, 3)
print(Employee.is_work_day(my_date))

#print(emp_1)
#print(repr(emp_1))
#print(str(emp_1))

emp_str_1 = 'Henry-Dickenson-56700'
new_emp_1 = Employee.from_string(emp_str_1)
print(new_emp_1.fullName())

Employee.set_raise_amt(1.05)
#print("Employee 1: {} {}".format(emp_1.first, emp_1.last), "Raised Amount: {}".format(emp_1.raise_amt))  #to get the full name of emp_1

#Let us now call the method 'fullName'
#Two ways to call the method
print(emp_1.fullName())   OR print(Employee.fullName(emp_1))   #--> this is how the system is actually understanding the previous way

#Defining instance variables - i.e. defined at each instance

emp_1.first = "Mimansa"
emp_1.last = "Gupta"
emp_1.email = 'MmmGgg@Oops.com'
emp_1.pay = "3000"

emp_2.first = "test"
emp_2.last = "user"
emp_2.email = 'testuser@Oops.com'
emp_2.pay = "900"

print(emp_1.email)
print(emp_2.email)
print(emp_2.pay)

emp_1.first = "Sample Test"
print(emp_1.fullName)
print(emp_1.email)
del emp_1.fullName
print(emp_1.total_pay(100, 200))
"""    

#INHERITANCE - sub-classes inheriting/adopting the properties and attributes of the parent class 
#&
#POLYMORPHISM - achieving many forms - basically through - 'method overriding' & 'method overloading'
#NOTE - In Python, 'method overloading' - '*args' & '*kwargs'
#NOTE - Other ways of achieving Polymorphism in Python - 'Dunder/Special/Magic' Methods

class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, **details):  #**details - **kwargs
        #Rather than redefining that entire block of __init__ method, we can use 'super()' method - Method Overriding
        super().__init__(first, last, pay)
        #Employee().__init__(self, fist, last, pay)  is also a way to write
        self.details = details

dev1 = Developer("Mimansa", "Gupta", 150000, role = "Developer", languageUsed = "Python", field = "AI/ML Engineer", branch = "Mumbai")
dev2 = Developer("Test", "Employee", 90000, role = "Developer", languageUsed = "C++", field = "Game Development", location = "Pune")
print(dev1.fullName)
print(dev1.details)
"""
print(dev1.pay)
dev1.apply_raise()  #as soon as we defined the fn under Developer class, the apply_raise() method worked accordingly
print(dev1.pay)
"""

class Manager(Employee):

    def __init__(self, first, last, pay, emp = None):
        super().__init__(first, last, pay)
        if emp is None:
            self.emp = []
        else:
            self.emp = emp

    def add_emp(self, emp):
        if emp not in self.emp:
            self.emp.append(emp)

    def remove_emp(self, emp):
        if emp in self.emp:
            self.emp.remove(emp)

    def listing_emp(self):
        print("Manages Employees-")
        for emp in self.emp:
            print("-->", emp.fullName())
    
mgr1 = Manager("Sue", "Smith", 80000, [dev1])
"""
print("Manager's Information-")
print("Full Name: ", mgr1.fullName())
print("Email Address: ", mgr1.email)
#mgr1.listing_emp()
mgr1.add_emp(emp_1)
mgr1.listing_emp()
print(dev1.progrmLang)
"""

"""
Some helpful built-in methods related to Classes and Objects - 
_______________________________________________________________________
print(isinstance(mgr1, Employee))    #to check whether an obj is an instance of a class, here mgr1 is an instance of both 'Employee' & 'Manager' classes, but not of the 'Developer' class
print(help(Developer))               #to know the structure of our class and sub-class
print(issubclass(Developer, Employee))  #to check whether a class is sub class of another
"""

