class ITargetPage(object):
    def __init__(self, site_name, email_as_account, site_description=''):
        self.site_name = site_name
        self.site_description = site_description
        self.email_as_account = email_as_account

    # Params:
    #   possible_account_list: a list of account str which wanted to be checked
    #   possible_email_list: a list of email str which wanted to be checked
    #
    # Return:
    #   a list of tupple in the form below:
    #       [
    #           (account_name: str, account_exist: bool),
    #           ...
    #       ]
    def check_result(self, possible_account_list, possible_email_list):
        pass
