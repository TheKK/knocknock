import json

import requests

from interfaces import ITargetPage

# FIXME This won't work everytime
class Target_page(ITargetPage):
    def __init__(self):
        super().__init__('Steam', email_as_account=False)

    def check_result(self, possible_account_list):
        result = []

        for account in possible_account_list:
            url = 'https://store.steampowered.com/join/checkavail/?accountname=%s&count=1' % account
            r = requests.get(url)
            content_json = json.loads(r.content.decode('utf-8'))

            if content_json['bAvailable'] == True:
                result.append((account, False))
            else:
                result.append((account, True))

        return result
