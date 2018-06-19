#!/usr/bin/env python
#coding: utf8

"""
project: TornadoServer
create date: 2018/6/19 
__author__ = xiashuangxi
"""


from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
engine = create_engine('mysql://test:test@localhost:3306/TornadoServer?charset=utf8', encoding="utf8", echo=False)
BaseDB = declarative_base()


ERROR_CODE = {
    "0": "ok",
    #Users error code
    "1001": "入参非法",
"1002": "用户已注册，请直接登录",
}
