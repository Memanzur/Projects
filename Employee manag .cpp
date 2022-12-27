#include <iostream>
#include <string>
#include <vector>


using namespace std;

// Employee managment software
class Employee {
public:
Employee(string name, int age, double salary)
: name_(name), age_(age), salary_(salary) {}

string getName() const { return name_; }
int getAge() const { return age_; }
double getSalary() const { return salary_; }

private:
string name_;
int age_;
double salary_;
};

// Employee management system class
class EmployeeManagementSystem {
public:
void addEmployee(const Employee& employee) {
employees_.push_back(employee);
}

void listEmployees() const {
for (const auto& employee : employees_) {
cout << "Name: " << employee.getName() << ", Age: " << employee.getAge()
<< ", Salary: " << employee.getSalary() << endl;
}
}

double averageSalary() const {
double total = 0;
for (const auto& employee : employees_) {
total += employee.getSalary();
}
return total / employees_.size();
}

private:
vector<Employee> employees_;
};

int main() {
EmployeeManagementSystem ems;
ems.addEmployee(Employee("Alice", 30, 100000));
ems.addEmployee(Employee("Bob", 35, 125000));
ems.addEmployee(Employee("Charlie", 40, 150000));

cout << "Employee list:" << endl;
ems.listEmployees();

cout << "Average salary: " << ems.averageSalary() << endl;

return 0;
}