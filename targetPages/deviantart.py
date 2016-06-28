import requests

from interfaces import ITargetPage

class Target_page(ITargetPage):
    def __init__(self):
        super().__init__('deviantart', email_as_account=False)

    def check_result(self, possible_account_list):
        result = []

        for account in possible_account_list:
            url = 'http://%s.deviantart.com/' % account
            r = requests.get(url)

            if r.status_code == 404:
                result.append((account, False))
            else:
                result.append((account, True))

        return result
