class HeaderMenu:

    def __init__(self, driver):
        self.driver = driver
        self.__sign_off_link_text = "Logout"
        self.__pim_link_id = "menu_pim_viewPimModule"

    def click_sign_off(self):
        self.driver.find_element_by_link_text(self.__sign_off_link_text).click()

    def naviagte_to_employee_listing(self):
        self.driver.find_element_by_id(self.__pim_link_id).click()

