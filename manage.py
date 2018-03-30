# -*- coding:utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_wtf.csrf import CSRFProtect
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
# session在flask中的扩展包
from flask_session import Session
from config import Config


app = Flask(__name__)

# 加载配置
app.config.from_object(Config)

# 创建连接到mysql数据库的对象
db = SQLAlchemy(app)

# 创建连接到redis数据库的对象
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)

# 开启CSRF保护
CSRFProtect(app)

# 创建脚本管理器对象
manager = Manager(app)

# 让app和db在迁移时建立关联
Migrate(app, db)
# 将数据库迁移脚本添加到甲苯管理器
manager.add_command('db', MigrateCommand)

# 使用session在flask扩展实现将session数据存储在redis
Session(app)


@app.route('/', methods=['GET', 'POST'])
def index():

    # 测试redis数据库
    redis_store.set('name', 'sz07')

    # 测试session:flask自带的session模块，用于存储session
    from flask import session
    session['name'] = 'sz07sz07'

    return 'index'


if __name__ == '__main__':
    # app.run()

    manager.run()