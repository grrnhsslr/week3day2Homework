# Create an Employee class that sets an employee's first name, last name, job title, salary, and email.
# The Employee class should have a class attribute for the raise amount set to 5% (1.05).
# Create a method that will apply the raise to an employee's salary.

# Write the Employee Parent Class Here
class Employee:
    raise_amount = 1.05

    def __init__(self, firstname, lastname, jobtitle, salary):
        self.firstname = firstname
        self.lastname = lastname
        self.jobtitle = jobtitle
        self.salary = salary
        self.email = f'{firstname}{lastname}@job.com'

    def salary_increase(self):
        self.salary = self.salary * self.raise_amount

# Create two more classes that inherit from the Employee class. One for Sales and one for Development.
# Both of these classes will have the same attributes as the Employee.
# For the Sales employees, add a phone number attribute on instantiation using the super method.
# Create a method on the Sales class that will "Send a Follow-Up Email". It should take in a customer name and "send"
# aka print a formatted email "Dear customer, Thank you for your interest in our product.
# Please let me know if you have any questions. My email is email or my phone number is phone number. Thanks, full name"
# Create an instance of a Sales Employee with a salary of $50,000.
# Write the Sales child Class Here


class Sales(Employee):
    def __init__(self, phone_number, firstname, lastname, jobtitle, salary):
        super().__init__(firstname, lastname, jobtitle, salary)
        self.phone_number = phone_number

    def follow_up(self, customer_name):
        print(f"Dear {customer_name}, Thank you for your interest in our product. Please let me know if you have any questions. My email is {self.email} or my phone number is {self.phone_number}. Thanks, {self.firstname} {self.lastname}")

# Create a method on the Development class called code that will print out "full name is writing code".
# Write the Development child Class Here


class Development(Employee):
    def __init__(self, firstname, lastname, jobtitle, salary):
        super().__init__(firstname, lastname, jobtitle, salary)

    def code(self):
        return f"{self.firstname} {self.lastname} is writing code"

# Send follow-up emails to "Mike O'Neil" and "Hannah Stern"


sales_employee = Sales("123-867-5309", "joe", "Smith", "sales", 50000)
sales_employee.follow_up("Mike O'Neil")
sales_employee.follow_up("Hannah Stern")

# Give the employee a raise and print the salary
sales_employee.salary_increase()
print(sales_employee.salary)

# Create an instance of a Development Employee with a salary of $100,000
dev_employee = Development("dave", "joe", "Smith", 100000)

# Write some code (call code method)
print(dev_employee.code())
# Give the dev employee a raise
dev_employee.salary_increase()
print(dev_employee.salary)
