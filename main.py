from icecream import ic
from src.tests.PagesAvailability import PagesAvailability


pa = PagesAvailability()
ic(pa.get_response_code('https://www.saucedemo.com/'))