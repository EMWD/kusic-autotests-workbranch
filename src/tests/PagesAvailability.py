from icecream import ic
import requests


class PagesAvailability():
    def __init__(self):
        pass

    def is_available(self, page: str, redirects=True) -> bool:
        try:
            response = requests.get(page, allow_redirects=redirects)
        except Exception:
            return False

        if response.status_code == 200:
            return True
        return False

    def check_availability(self, pages: dict, pages_base: str=None, redirects=True) -> dict:
        '''Return dict with "key" = "site_name", and "value" = "is_page_available" '''
        res = {}
        if pages_base:
            for page in pages:
                res[pages_base + page] = self.is_available(pages_base + page, redirects=redirects)
            return res

        for page in pages:
            res[page] = self.is_available(page, redirects=redirects)    
        return res

    def get_response_code(self, page: str) -> int:
        try:
            return requests.get(page, allow_redirects=False).status_code
        except Exception:
            return 0
