# login test

from src.tests.Login import Login

form_data = {
   'login_field': {'obj':'id_username', 'by':'id'},
   'password_field': {'obj':'id_password', 'by':'id'},
   'button': {'obj':'btn-primary', 'by':'class'},
   'login': 'admin2',
   'password': 'SOME_PASSWORD',
}
check_data = {
   'search_by': 'class',
   'find': 'title',
   'value': "It's time to use Bot in your server"
}
l = Login('https://langa.xyz/login', form_data=form_data, check_data=check_data)
l.login_test()

#available test

from src.tests.PagesAvailability import PagesAvailability

pages = {
    'https://langa.xyz/': None,
    'https://langa.xyz/commands/': None,
    'https://langa.xyz/features/': None,
    'https://langa.xyz/donate/': None,
    'https://langa.xyz/login': None,
    'https://langa.xyz/register': None,
}
pa = PagesAvailability()
res = pa.check_availability(pages=pages, redirects=True)

# OR

pages_base = 'https://langa.xyz/'
pages = {
    '',
    'commands/',
    'features/',
    'donate/',
    'login',
    'register',
}
pa = PagesAvailability()
res = pa.check_availability(pages=pages, pages_base=pages_base, redirects=True)