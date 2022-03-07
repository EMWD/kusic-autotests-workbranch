from time import sleep
from src.WebDriver import WebDriver
from selenium.webdriver.common.keys import Keys
from icecream import ic

class Auth():
    def __init__(self, site, form_data, check_data=None, method='local'):
        self.driver_ = WebDriver(method).get_driver()
        self.driver_.get(site)
        self.form_data_ = form_data
        self.check_data_ = check_data

    def custom_search(self, obj, by):
        match by:
            case "class":
                return self.driver_.find_element_by_class_name(obj)
            case "id":
                return self.driver_.find_element_by_id(obj)
            case "name":
                return self.driver_.find_element_by_name(obj)
            case "tag":
                return self.driver_.find_element_by_tag_name(obj)
            case "custom":
                return self.driver_.find_elements_by_xpath(f"//label[@for='exampleInputEmail1']")


    def test_login(self):
        # Elems search
        input_username = self.custom_search(self.form_data_.get('login_field').get('obj'), self.form_data_.get('login_field').get('by'))
        input_password = self.custom_search(self.form_data_.get('password_field').get('obj'), self.form_data_.get('password_field').get('by'))
        login_button = self.custom_search(self.form_data_.get('button').get('obj'), self.form_data_.get('button').get('by'))

        # Forms interaction
        input_username.send_keys(self.form_data_.get('login'))
        input_password.send_keys(self.form_data_.get('password'))
        login_button.send_keys(Keys.RETURN)
        
        sleep(3)

        # On page check
        if self.check_data_:
            title_text = self.custom_search(self.check_data_.get('find'), self.check_data_.get('search_by'))
            if title_text.text == self.check_data_.get('value'):
                print("This is main page")
            else:
                print("SEARCH ERROR")

        
    def test_registration(self):
        # Elems search
        input_username = self.custom_search(self.form_data_.get('login_field').get('obj'), self.form_data_.get('login_field').get('by'))
        input_email = self.custom_search(self.form_data_.get('email_field').get('obj'), self.form_data_.get('email_field').get('by'))
        input_password = self.custom_search(self.form_data_.get('password_field').get('obj'), self.form_data_.get('password_field').get('by'))
        input_password2 = self.custom_search(self.form_data_.get('password_field2').get('obj'), self.form_data_.get('password_field2').get('by'))
        capcha_field = self.custom_search(self.form_data_.get('capcha_field').get('obj'), self.form_data_.get('capcha_field').get('by'))
        capcha_answer = self.custom_search(self.form_data_.get('capcha_answer').get('obj'), self.form_data_.get('capcha_answer').get('by'))
        reg_button = self.custom_search(self.form_data_.get('reg_button').get('obj'), self.form_data_.get('reg_button').get('by'))

        # Forms interaction
        input_username.send_keys(self.form_data_.get('login'))
        input_email.send_keys(self.form_data_.get('email'))
        input_password.send_keys(self.form_data_.get('password'))
        input_password2.send_keys(self.form_data_.get('password'))
        capcha_full = capcha_answer[4].get_attribute("textContent")
        capcha = capcha_full.split(' ')
        num1, sign, num2 = capcha[3], capcha[4], capcha[5] 
        if sign == '+':
           capcha_answer = int(num1) + int(num2)
        elif sign == '-':
           capcha_answer = int(num1) - int(num2)

        capcha_field.send_keys(capcha_answer)
        reg_button.send_keys(Keys.RETURN)