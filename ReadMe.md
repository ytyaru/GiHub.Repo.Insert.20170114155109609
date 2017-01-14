# このソフトウェアについて

指定ユーザのGitHubリポジトリ情報をDBに挿入する。

# 開発環境

* Windows XP Pro SP3 32bit
    * cmd.exe
* [Python 3.4.4](https://www.python.org/downloads/release/python-344/)
    * [requests](http://requests-docs-ja.readthedocs.io/en/latest/)
    * [dataset](https://github.com/pudo/dataset)
    * [furl](https://github.com/gruns/furl)

## WebService

* [GitHub](https://github.com/)
    * [アカウント](https://github.com/join?source=header-home)
    * [AccessToken](https://github.com/settings/tokens)
    * [Two-Factor認証](https://github.com/settings/two_factor_authentication/intro)
    * [API v3](https://developer.github.com/v3/)

# 準備

* [GitHubアカウント](https://github.com/join?source=header-home)を作成する
* `repo`権限をもつ[AccessToken](https://github.com/settings/tokens)を作成する
* [GitHub.Accounts.Database](https://github.com/ytyaru/GitHub.Accounts.Database.20170107081237765)でGitHubアカウントDBを作成する
* [GitHub.Repositories.Database.Create](https://github.com/ytyaru/GitHub.Repositories.Database.Create.20170114123411296)でGitHubリポジトリDBを作成する
* Main.pyにて以下の変数を設定する

```python
db_path_account = 'C:/GitHub.Accounts.sqlite3'
db_path_repo = 'C:/GitHub.Repositories.sqlite3'
username = 'github_username'
```

# 実行

```dosbatch
python Main.py
```

# 結果

指定ユーザのGitHubリポジトリ情報が`GiHubApi.Repositories.sqlite3`ファイルに保存される。

# ライセンス #

このソフトウェアはCC0ライセンスである。

[![CC0](http://i.creativecommons.org/p/zero/1.0/88x31.png "CC0")](http://creativecommons.org/publicdomain/zero/1.0/deed.ja)
