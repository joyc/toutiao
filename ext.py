#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : ext.py
# @Author : Hython
# @Date   : 公元 2020/03/18 21:26
import functools
import hashlib
from datetime import datetime

from sqlalchemy import (Column, DateTime, Interval, event, inspect)
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
from sqlalchemy.orm.interfaces import MapperOption
from sqlalchemy.orm.attributes import get_history
from sqlalchemy.ext.declarative import declared_attr
from dogpile.cache.region import make_region
from dogpile.cache.api import NO_VALUE
from flask_sqlalchemy import (SQLAlchemy, Model, BaseQuery, DefaultMeta, _QueryProperty)
from flask_security import Security

from config import REDIS_URL
from corelib.db import PropsMixin, PropsItem


def md5_key_mangler(key):
    if key.startwith('SELECT '):
        key = hashlib.md5(key.encode('ascii')).hexdigest()
    return key


