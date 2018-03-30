# -*- coding:utf-8 -*-


# from iHome import app, db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from iHome import get_app


# 创建app
app = get_app('development')


# 创建脚本管理器对象
manager = Manager(app)

# 让app和db在迁移时建立关联
# Migrate(app, db)
# 将数据库迁移脚本添加到甲苯管理器
manager.add_command('db', MigrateCommand)


@app.route('/', methods=['GET', 'POST'])
def index():

    # 测试redis数据库
    # redis_store.set('name', 'sz07')

    # 测试session:flask自带的session模块，用于存储session
    # from flask import session
    # session['name'] = 'sz07sz07'

    return 'index'


if __name__ == '__main__':
    # app.run()

    manager.run()