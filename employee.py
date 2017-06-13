class Employee(object):
    """
    Basic employee information that is available for both staff and managers
    """

    def __init__(self, user_id, email, department, has_basic_privileges=True, has_admin_privileges=False,
                 tasks_remaining=1):
        self.user_id = user_id
        self.email = email
        self.department = department
        self.basic_privileges = has_basic_privileges
        self.admin_privileges = has_admin_privileges
        self.tasks = tasks_remaining

    """
    An employee can agree to take on tasks from the board
    """

    def take_on_task(self, task_count):
        self.tasks += task_count
        return self.tasks

    """
    After finishing a task an employee can tick it off from the board
    """

    def tick_off_task(self, task_count):
        self.tasks -= task_count
        return self.tasks


class Admin(object):
    """
    Admin can has privileges such as removing an employee
    """

    def __init__(self, admin_key, can_drop_employee=True, can_view_employee=True):
        self.admin_key = admin_key
        self.can_drop_employee = can_drop_employee
        self.can_view_employee = can_view_employee


    """
    Staff inherits from Employee. There is an 'is a' relationshp
    """


class Staff(Employee):
    def __init__(self, hourly=True, paid_daily=True):
        self.hourly = hourly
        self.paid_daily = paid_daily
        self.__wages = 0


    """
    Encapsulation.
    Wages are private variables and can only be changes using a setter
    """
    def set_wages(self, wages):
        self.__wages = wages

    """
    Manager inherits from Employee and Admin. It is Polymorphic
    """
class Manager(Employee, Admin):
    def __init__(self, monthly=True, paid_monthly=True):
        self.monthly = monthly
        self.paid_monthly = monthly
        self.__salary = 0

    """
    Encapsulation.
    Salaries are private variables and can only be set using a setter
    """
    def set_salary(self, salary):
        self.__salary = salary
