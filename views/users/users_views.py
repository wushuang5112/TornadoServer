#! /usr/bin/python3
# -*- coding:utf-8 -*-

import tornado.web
from tornado.escape import json_decode
import logging
from logging.handlers import TimedRotatingFileHandler

# 从commons中导入http_response方法
from common.commons import (
    http_response,
)

# 从配置文件中导入错误码
from conf.base import (
    ERROR_CODE,
)

########## Configure logging #############
logFilePath = "log/users/users.log"
logger = logging.getLogger("Users")
logger.setLevel(logging.DEBUG)
handler = TimedRotatingFileHandler(logFilePath,
                                   when="D",
                                   interval=1,
                                   backupCount=30)
formatter = logging.Formatter('%(asctime)s \
%(filename)s[line:%(lineno)d] %(levelname)s %(message)s',)
handler.suffix = "%Y%m%d"
handler.setFormatter(formatter)
logger.addHandler(handler)


class RegistHandle(tornado.web.RequestHandler):
    """handle /user/regist request
    :param phone: users sign up phone
    :param password: users sign up password
    :param code: users sign up code, must six digital code
    """

    def post(self):
        try:
            # 获取入参
            args = json_decode(self.request.body)
            phone = args['phone']
            password = args['password']
            verify_code = args['code']
        except:
            #获取入参失败时，抛出错误码及错误信息
            logger.info("RegistHandle: request argument incorrect")
            # 获取入参失败时，抛出错误码及错误信息
            http_response(self, ERROR_CODE['1001'], 1001)
            return

        # 处理成功后，返回成功码“0”及成功信息“ok”
        logger.debug("RegistHandle: regist successfully")
        http_response(self, ERROR_CODE['0'], 0)
