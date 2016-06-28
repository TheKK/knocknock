import requests

from interfaces import ITargetPage

class Target_page(ITargetPage):
    def __init__(self):
        super().__init__('InkBunny', email_as_account=False)

    def check_result(self, possible_account_list):
        result = []

        for account in possible_account_list:
            url = 'https://inkbunny.net/%s' % account
            r = requests.get(url)

            if r.url == url:
                result.append((account, True))
            else:
                result.append((account, False))

        return result
