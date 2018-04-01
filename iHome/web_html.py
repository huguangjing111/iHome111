# -*- coding:utf-8 -*-


from flask import Blueprint, current_app


html_blue = Blueprint('html_blue', __name__)


@html_blue.route('/<file_name>')
def get_static_html(file_name):
    """获取静态文件"""
    # 需求1：http://127.0.0.1:5000/login.html

    # 拼接file_name所在的路径 '/static/html/login.html'
    # 拼接file_name所在的路径 '/static/html/file_name'

    file_path = 'html/' + file_name

    # 使用file_path去查找指定路径下的静态html
    return current_app.send_static_file(file_path)