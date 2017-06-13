import unittest
from employee import Employee,Staff,Admin,Manager

class EmployeeTestCase(unittest.TestCase):

    def setUp(self):
        self.my_employee = Employee(1234,"zmn@organization.com",department='IT')
        self.staff = Staff()

    def test_admin_priveleges_false(self):
        self.assertEqual(self.my_employee.admin_privileges,False,msg="An employee does not have admin privileges by default")


    def test_basic_privileges_true(self):
        self.assertEqual(self.my_employee.basic_privileges,True, msg="An employee has basic priveleges by default")

    def test_employee_can_take_on_task(self):
        self.my_employee.take_on_task(1)
        self.assertEqual(self.my_employee.tasks,2,msg="Task adding method inaccurate")

    def test_employee_can_tick_off_task(self):
        self.my_employee.tick_off_task(1)
        self.assertEqual(self.my_employee.tasks,0,msg="Task adding method inaccurate")

    def test_staff_is_subclass_of_employee(self):
        self.assertTrue(issubclass(Staff,Employee),msg="Staff not subclass of Employee")

    def test_manager_is_subclass_of_admin(self):
        self.assertTrue(issubclass(Manager,Admin),msg="Manager not subclass of Employee")



