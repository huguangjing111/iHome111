# -*- coding:utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis


class Config(object):
    """加载配置"""

    # 开启调试模式
    DEBUG = True

    # 配置mysql数据库:开发中使用真实IP
    SQLALCHEMY_DATABASE_URI = 'mysql://root:mysql@127.0.0.1:3306/iHome_07'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # 配置redis数据库：开发中使用真实IP
    REDIS_HOST = '127.0.0.1'
    REDIS_PORT = 6379



app = Flask(__name__)

# 加载配置
app.config.from_object(Config)

# 创建连接到mysql数据库的对象
db = SQLAlchemy(app)

# 创建连接到redis数据库的对象
redis_store = redis.StrictRedis(host=Config.REDIS_HOST, port=Config.REDIS_PORT)


@app.route('/')
def index():

    # 测试redis数据库
    redis_store.set('name', 'sz07')

    return 'index'


if __name__ == '__main__':
    app.run()