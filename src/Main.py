#!python3
#encoding:utf-8

import os
from pathlib import Path
from github import Repository
from sqlite import Account
from sqlite import Insert
from datetime import datetime
import json

def get_created_datetime(json_file_path):
    return datetime.fromtimestamp(os.stat(json_file_path).st_mtime)

db_path_account = 'C:/GitHub.Accounts.sqlite3'
db_path_repo = 'C:/GitHub.Repositories.sqlite3'
username = 'github_username'

account = Account.Account(db_path_account)
account.set_username(username)

repo = Repository.Repository()
ins = Insert.Insert(db_path_repo)

json_file_path = "./GiHubApi.Repositories.{0}.json".format(username)
if os.path.exists(json_file_path):
    with open(json_file_path, 'r') as f:
        j = json.loads(f.read())
        ins.insert(j, get_created_datetime(json_file_path))
else:
    j = None
    if (account.get_otp() is None):
        j = repo.gets(token=account.get_token())
    else:
        j = repo.gets(otp=account.get_otp(), token=account.get_token())
    ins.insert(j, datetime.now())
