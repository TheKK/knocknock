import requests

from interfaces import ITargetPage

class Target_page(ITargetPage):
    def __init__(self):
        super().__init__('Pixiv', email_as_account=False)

    def check_result(self, possible_account_list):
        result = []

        for account in possible_account_list:
            account = account.lower() # Pixiv use lowercase account name
            url = 'http://pixiv.me/%s' % account
            r = requests.get(url)

            if r.status_code == 404:
                result.append((account, False))
            else:
                result.append((account, True))

        return result
