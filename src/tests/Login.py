from src.WebDriver import WebDriver
from selenium.webdriver.common.keys import Keys


class Login():
    def __init__(self, site, form_data, method='local'):
        self.driver_ = WebDriver(method).get_driver()
        self.driver_.get(site)
        self.form_data_ = form_data


    def login_test(self):
        # Elems search
        input_username = self.driver_.find_element_by_xpath(f"//*[@id=\"{self.form_data_.get('login_field_id')}\"]")
        input_password = self.driver_.find_element_by_xpath(f"//*[@id=\"{self.form_data_.get('password_field_id')}\"]")
        login_button = self.driver_.find_element_by_xpath(f"//*[@id=\"{self.form_data_.get('button')}\"]")

        # Forms interaction
        input_username.send_keys(self.form_data_.get('login'))
        input_password.send_keys(self.form_data_.get('password'))
        login_button.send_keys(Keys.RETURN)

        # On page check
        title_text = self.driver_.find_element_by_xpath("//*[@id=\"header_container\"]/div[2]/span")
        if title_text.text == "PRODUCTS":
            print("This is main page")
        else:
            print("Search error")