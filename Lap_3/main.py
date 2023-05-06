from person import Person
from employee import Employee
from office import Office

employees = [Employee("samy", 10000, 10, 200), Employee("ALi", 10000, 10, 200)]

office = Office("ITI", employees)

office.get_All_employees()
