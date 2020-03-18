#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : index.py
# @Author : Hython
# @Date   : 公元 2020/03/19 0:01
from flask.blueprints import Blueprint

bp = Blueprint('index', __name__)


@bp.route('/')
def index():
    return 'Index'
