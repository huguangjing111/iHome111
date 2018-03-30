# -*- coding:utf-8 -*-
from werkzeug.routing import BaseConverter


from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import redis
from flask_wtf.csrf import CSRFProtect
# session在flask中的扩展包
from flask_session import Session
# from config import Config, DevelopmentConfig, ProductionConfig
from config import configs


# 创建可以被外界导入的数据库连接对象
db = SQLAlchemy()
# 创建可以被外界导入的连接到redis数据库的对象
redis_store = None


# default_config == config_name
def get_app(config_name):
    """工厂方法：根据不同的配置信息，实例化出不同的app"""

    app = Flask(__name__)

    # 加载配置
    app.config.from_object(configs[config_name])

    # 创建连接到mysql数据库的对象
    # db = SQLAlchemy(app)
    db.init_app(app)

    # 创建连接到redis数据库的对象
    global redis_store
    redis_store = redis.StrictRedis(host=configs[config_name].REDIS_HOST, port=configs[config_name].REDIS_PORT)

    # 开启CSRF保护
    CSRFProtect(app)

    # 使用session在flask扩展实现将session数据存储在redis
    Session(app)

    return app
