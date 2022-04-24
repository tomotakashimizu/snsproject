# how-to-create-django-project

python を使った開発を行う時は、プロジェクトごとに実行環境を作成し、それらの環境を切り替えて使用するのが一般的です。

venv を使うと pip でインストールしたパッケージをプロジェクトごとに独立させることができます。

## ディレクトリの作成

```
$ mkdir snsproject
$ cd snsproject
```

## .gitignore の作成

## Initial commit

## 新しい環境の作成

```
$ python3 -m venv venv
```

## 仮想環境の起動

```
$ source venv/bin/activate
(venv) $
```

## Django のインストール

```
#最新バージョンのDjangoをインストール
(venv) $ pip install django

#バージョンの確認
venv ❯ python3 -m django --version
4.0.4
```

## プラグインのインストール

```
# Pythonのフォーマッタをインストール
# https://qiita.com/psychoroid/items/2c2acc06c900d2c0c8cb
(venv) $ pip install flake8
# https://zenn.dev/yhay81/articles/yhay81-202102-pythonlint
(venv) $ pip install black
(venv) $ pip install tox
(venv) $ pip install isort
(venv) $ pip install mypy
(venv) $ pip install bandit
```

## .vscode/settings.json を設定

## .unibeautifyrc.json を設定

## tox.ini を設定

## setup.cfg を設定

## startproject

```
# pwdはここ ~/Documents/Python/Django/Udemy/django-3app/snsproject
venv ❯ ls
venv

(venv) $ django-admin startproject snsproject .
```

## Django プロジェクトを localhost で実行する

```
(venv) $ python manage.py runserver
```

## Django App を作成する

```
(venv) $ python manage.py startapp snsapp
```

## models.py の作成・実行

データベースにテーブルを作成する。

### makemigrations

```
(venv) $ python manage.py makemigrations

#プロジェクト上に複数のアプリがある場合は[アプリ名]をつける
(venv) $ python manage.py makemigrations [アプリ名]

(venv) $ python manage.py makemigrations snsapp
```

### migrate

```
(venv) $ python manage.py migrate
```

## 管理画面と createsuperuser

管理する user を作成する。

```
(venv) $ python manage.py createsuperuser
```

## 仮想環境の停止

```
(venv) $ deactivate
$
```
