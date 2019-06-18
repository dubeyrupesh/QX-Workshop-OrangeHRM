class EmployeePage:

    def __init__(self, driver):
        self.driver = driver
        self.__add_employee_link_id = "menu_pim_addEmployee"
        self.__first_name_link_id = "firstName"
        self.__last_name_link_id = "lastName"
        self.__save_btn_id = "btnSave"

    def add_employee(self, first_name, last_name):
        self.driver.find_element_by_id(self.__add_employee_link_id).click()
        self.driver.find_element_by_id(self.__first_name_link_id).send_keys(first_name)
        self.driver.find_element_by_id(self.__last_name_link_id).send_keys(last_name)
        self.driver.find_element_by_id(self.__save_btn_id).click()
