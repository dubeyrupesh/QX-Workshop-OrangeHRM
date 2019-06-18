from selenium import webdriver
import unittest
import HtmlTestRunner
from Pages.loginPage import LoginPage
from Pages.headerMenu import HeaderMenu
from Pages.employeePage import EmployeePage
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), "...", "..."))

class LoginTest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.fullscreen_window()

    def test_login(self):
        driver = self.driver
        login = LoginPage(driver)
        header = HeaderMenu(driver)
        employee = EmployeePage(driver)

        employee_first_name = "First_Name"
        employee_last_name = "Last_Name"

        driver.get("https://opensource-demo.orangehrmlive.com/index.php/auth/login")

        login.enter_username("admin")
        login.enter_password("admin123")

        login.click_login()
        header.naviagte_to_employee_listing()

        employee.add_employee(employee_first_name, employee_last_name)

    @classmethod
    def tearDownClass(cls):
        cls.driver.close()
        cls.driver.quit()


if __name__ == "__main__":
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output='reports/'))
