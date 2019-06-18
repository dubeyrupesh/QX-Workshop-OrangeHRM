class LoginPage:

    def __init__(self, driver):
        self.__driver = driver

        # Locators - Private members
        self.__userName_textbox_id = "txtUsername"
        self.__password_textbox_id = "txtPassword"
        self.__login_button_id = "btnLogin"

    def enter_username(self, username):
        self.__driver.find_element_by_id(self.__userName_textbox_id).send_keys(username)

    def enter_password(self, password):
        self.__driver.find_element_by_id(self.__password_textbox_id).send_keys(password)

    def click_login(self):
        self.__driver.find_element_by_id(self.__login_button_id).click()

