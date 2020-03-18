#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : user.py
# @Author : Hython
# @Date   : 公元 2020/03/18 10:52
import os
import requests
from sqlalchemy import func as alchemyFn
from flask_security import SQLAlchemyUserDatastore, UserMixin, RoleMixin

from ext import db

