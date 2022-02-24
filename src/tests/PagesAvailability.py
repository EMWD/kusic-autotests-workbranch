from icecream import ic
import requests


class PagesAvailability():
    def __init__(self):
        pass

    def is_available(self, page: str) -> bool:
        try:
            response = requests.get(page, allow_redirects=False)
        except Exception:
            return False

        if response.status_code == 200:
            return True
        return False

    def check_availability(self, pages: dict) -> dict:
        res = {}
        for page in pages:
            res[page] = self.is_available(page)
        return res

    def get_response_code(self, page: str) -> int:
        try:
            return requests.get(page, allow_redirects=False).status_code
        except Exception:
            return 0
