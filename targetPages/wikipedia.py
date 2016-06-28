import requests

from interfaces import ITargetPage

class Target_page(ITargetPage):
    def __init__(self):
        super().__init__('Wikipedia', email_as_account=False)

    def check_result(self, possible_account_list):
        result = []

        for account in possible_account_list:
            url = 'https://en.wikipedia.org/wiki/User:%s' % account
            r = requests.get(url)

            if r.content.decode('utf-8').find('is not registered.') >= 0:
                result.append((account, False))
            else:
                result.append((account, True))

        return result
