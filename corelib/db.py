#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @File   : db.py
# @Author : Hython
# @Date   : 公元 2020/03/18 23:37
import copy
import json
from datetime import datetime

from walrus import Database

from config import REDIS_URL
from corelib.local_cache import lc

rdb = Database.from_url(REDIS_URL)


class PropsMixin:

    @property
    def _props_name(self):
        '''
        为了保证能够与corelib.mixin.wrapper能和谐的工作
        需要不同的class有不同的__props以免冲突
        '''
        return '__%s/props_cached' % self.get_uuid()

    @property
    def _props_db_key(self):
        return '%s/props' % self.get_uuid()

    def _get_props(self):
        props = lc.get(self._props_name)
        if props is None:
            props = rdb.get(self._props_db_key) or ''
            props = props and json.loads(props) or {}
            lc.set(self._props_name, props)
        return props

    def _set_props(self, props):
        rdb.set(self._props_db_key, json.dumps(props))
        lc.delete(self._props_name)

    def _destory_props(self):
        rdb.delete(self._props_db_key)
        lc.delete(self._props_name)

    _destroy_props = _destory_props

    get_props = _get_props
    set_props = _set_props

    props = property(_get_props, _set_props)

