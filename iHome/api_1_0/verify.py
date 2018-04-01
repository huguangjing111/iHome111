# -*- coding:utf-8 -*-
# 图片验证码和短信验证码


from . import api
from iHome.utils.captcha.captcha import captcha


@api.route('/image_code')
def get_image_code():
    """提供图片验证码"""

    # 生成验证码:text是验证码的文字信息，image验证码的图片信息
    name, text, image = captcha.generate_captcha()

    # 响应验证码
    return image