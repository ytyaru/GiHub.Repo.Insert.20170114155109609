#!python3
#encoding:utf-8

import dataset
from tkinter import Tk
from datetime import datetime
import traceback

class Insert:
    def __init__(self, db_path):
        self.db = dataset.connect('sqlite:///' + db_path)

    """
    Insert json data into the DB.
    @params [dict] repositories. [List your repositories API](https://developer.github.com/v3/repos/#list-your-repositories) response.
    """
    def insert(self, repos, repos_datetime):
        for r in repos:
            try:
                self._insert_Repositories(r, repos_datetime)
                self._insert_Counts(r)
            except:
                traceback.print_exc()

    def _insert_Repositories(self, r, repos_datetime):
        self.db['Repositories'].insert(dict(
            IdOnGitHub=r['id'], 
            Name=r['name'], 
            Description=r['description'], 
            Homepage=r['homepage'], 
            CreatedAt=r['created_at'], 
            PushedAt=r['pushed_at'], 
            UpdatedAt=r['updated_at'], 
            CheckedAt="{0:%Y-%m-%d %H:%M:%S}".format(repos_datetime)))

    def _insert_Counts(self, r):
        repo = self.db['Repositories'].find_one(IdOnGitHub=r['id'])
        self.db['Counts'].insert(dict(
            RepositoryId=repo['Id'], 
            Forks=r['forks_count'], 
            Stargazers=r['stargazers_count'], 
            Watchers=r['watchers_count'], 
            Issues=r['open_issues_count']))

    def gets(self):
        for r in self.db['Repositories'].all():
            print(r)
        return self.db['Repositories'].all()
