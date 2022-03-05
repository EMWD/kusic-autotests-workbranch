from src.WebDriver import WebDriver
from selenium.webdriver.common.keys import Keys
from icecream import ic

class Login():
    def __init__(self, site, form_data, check_data, method='local'):
        self.driver_ = WebDriver(method).get_driver()
        self.driver_.get(site)
        self.form_data_ = form_data
        self.check_data_ = check_data

    def custom_search(self, obj, by):
        if by == 'class':
            return self.driver_.find_element_by_class_name(obj)
        elif by == 'id':
            return self.driver_.find_element_by_id(obj)

    def login_test(self):
        # Elems search
        input_username = self.custom_search(self.form_data_.get('login_field').get('obj'), self.form_data_.get('login_field').get('by'))
        input_password = self.custom_search(self.form_data_.get('password_field').get('obj'), self.form_data_.get('password_field').get('by'))
        login_button = self.custom_search(self.form_data_.get('button').get('obj'), self.form_data_.get('button').get('by'))

        # Forms interaction
        input_username.send_keys(self.form_data_.get('login'))
        input_password.send_keys(self.form_data_.get('password'))
        login_button.send_keys(Keys.RETURN)

        # On page check
        title_text = self.custom_search(self.check_data_.get('find'), self.check_data_.get('search_by'))
        if title_text.text == self.check_data_.get('value'):
            print("This is main page")
        else:
            print("SEARCH ERROR")