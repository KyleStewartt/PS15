class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
    def displayEmployee(self):
        print("Name: ", self.name, ", Salary: ", self.salary)
    def calculateBonus(self, bonusRate):
        return self.salary * bonusRate
class Manager(Employee):
    def __init__(self, name, salary):
        super().__init__(name, salary)
    def computeLongTermBonus(self):
        return self.salary * 0.4
def main():
    # Test Manager class
    manager1 = Manager("John Smith", 70000)
    manager1.displayEmployee()
    longTermBonus = manager1.computeLongTermBonus()
    print("Long Term Bonus: ", longTermBonus)
if __name__ == "__main__":
    main()