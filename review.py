class Employee:
    def __init__(self, base_salary):
        self.base_salary = base_salary

    def get_salary(self):
        return self.base_salary

class EmployeeManager:
    def __init__(self):
        self._employees = []
    def add_employee(self, employee):
        self._employees.append(employee)
    def calculate_total_salary(self):
        total_salary = 0
        for item in self._employees:
            total_salary += item.get_salary()
        return total_salary

class Programmer(Employee):
    def __init__(self, base_salary=0, bonus=0):
        super().__init__(base_salary)
        self.bonus = bonus

    def get_salary(self):
        return super().get_salary() + self.bonus


class Testor(Employee):
    def __init__(self, bugs, base_salary):
        super().__init__(base_salary)
        self.bugs = bugs
        print(self.bugs)
    def get_salary(self):
        return self.base_salary + self.bugs * 5

manager = EmployeeManager()
manager.add_employee(Programmer(10000, 100000))
manager.add_employee(Testor(8000, 100))
print(manager.calculate_total_salary())
# 这是一行无关紧要的代码
