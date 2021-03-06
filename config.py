#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : config.py
# @Author : Hython
# @Date   : 公元 2020/03/18 23:10
import os

HERE = os.path.abspath(os.path.dirname(__file__))
REDIS_URL = 'redis://localhost:6379'
CACHE_REDIS_URL = REDIS_URL
DEBUG = False
UPLOAD_FOLDER = os.path.join(HERE, 'permdir')
SQLALCHEMY_RECORD_QUERIES = True
DATABASE_QUERY_TIMEOUT = 0.5
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = 'secretkey123'
TEMPLATES_AUTO_RELOAD = False
SECURITY_CONFIRMABLE = True
SECURITY_REGISTERABLE = True
SECURITY_RECOVERABLE = True
SECURITY_CHANGEABLE = True
SECURITY_TRACKABLE = True
SECURITY_POST_REGISTER_VIEW = SECURITY_POST_RESET_VIEW = SECURITY_POST_CONFIRM_VIEW = 'online.landing'  # noqa
SECURITY_PASSWORD_SALT = 'password234'

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:@localhost/video?charset=utf8mb4'  # noqa

SOCIAL_AUTH_USER_MODEL = 'models.user.User'
SOCIAL_AUTH_AUTHENTICATION_BACKENDS = (
    'social_core.backends.github.GithubOAuth2',
    'social_core.backends.weibo.WeiboOAuth2',
    'social_core.backends.douban.DoubanOAuth2',
    'social_core.backends.weixin.WeixinOAuth2'
)

SOCIAL_AUTH_GITHUB_KEY = ''
SOCIAL_AUTH_GITHUB_SECRET = ''
SOCIAL_AUTH_WEIBO_KEY = ''
SOCIAL_AUTH_WEIBO_SECRET = ''
SOCIAL_AUTH_WEIBO_DOMAIN_AS_USERNAME = True
SOCIAL_AUTH_DOUBAN_KEY = ''
SOCIAL_AUTH_DOUBAN_SECRET = ''
SOCIAL_AUTH_WEIXIN_KEY = ''
SOCIAL_AUTH_WEIXIN_SECRET = ''
SOCIAL_AUTH_LOGIN_REDIRECT_URL = '/'
SOCIAL_AUTH_REDIRECT_IS_HTTPS = True
CLEAN_USERNAMES = False
SOCIAL_AUTH_REMEMBER_SESSION_NAME = 'remember_me'
SOCIAL_AUTH_FIELDS_STORED_IN_SESSION = ['keep']

CACHE_TYPE = 'redis'

if not os.path.exists(UPLOAD_FOLDER):
    os.mkdir(UPLOAD_FOLDER)

try:
    from local_settings import *  # noqa
except ImportError:
    pass
