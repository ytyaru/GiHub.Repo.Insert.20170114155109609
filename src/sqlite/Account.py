#!python3
#encoding:utf-8

import dataset
from tkinter import Tk

class Account:
    def __init__(self, db_path):
        self.db_path = db_path
        self.db = dataset.connect('sqlite:///' + db_path)
        self.username = ''
        self.password = ''
        self.token = ''
        self.otp = ''

    def set_username(self, username):
        self.username = username
        account = self.db['Accounts'].find_one(Username=username)
        self.password = account['Password']
        self._get_otp_by_clipboard(account['Id'])
        self._get_access_token(account['Id'], ['repo', 'public_repo'])

    def _get_access_token(self, account_id, scopes):
        sql = "SELECT * FROM AccessTokens WHERE AccountId == {0} AND (".format(account_id)
        for s in scopes:
            sql = sql + "(',' || Scopes || ',') LIKE '%,{0},%'".format(s) + " OR "
        sql = sql.rstrip(" OR ")
        sql = sql + ')'
        print(sql)
        tokens = self.db.query(sql)
        for t in tokens:
           print(t)
           self.token = t['AccessToken']
        return self.token

    def _get_otp_by_clipboard(self, account_id):
        two_factor = self.db['TwoFactors'].find_one(AccountId = account_id)
        if not(two_factor is None):
            self.otp = Tk().clipboard_get()
        else:
            self.otp = None
        return self.otp

    def get_username(self):
        return self.username
    def get_password(self):
        return self.password
    def get_token(self):
        return self.token
    def get_otp(self):
        return self.otp
