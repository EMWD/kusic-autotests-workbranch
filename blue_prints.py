# login test

from src.tests.Login import Login

form_data = {
   'login_field_id': 'user-name',
   'password_field_id': 'password',
   'button': 'login-button',
   'login': 'standard_user',
   'password': 'secret_sauce',
}
l = Login('https://www.saucedemo.com/', form_data=form_data)
l.login_test()


#available test

from src.tests.PagesAvailability import PagesAvailability

pages = {
    'https://www.saucedemo.com/': None,
    'https://www.google.com/': None,
    'https://www.google.com/': None,
}
pa = PagesAvailability()
pa.check_pages_availability(pages)

