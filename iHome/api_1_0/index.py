# -*- coding:utf-8 -*-


from . import api


@api.route('/', methods=['GET', 'POST'])
def index():

    # 测试redis数据库
    # from iHome import redis_store
    # redis_store.set('name', 'heheheehehehehhe')

    # 测试session:flask自带的session模块，用于存储session
    # from flask import session
    # session['name'] = 'sz07sz07'

    return 'index'