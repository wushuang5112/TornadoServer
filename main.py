#!/usr/bin/env python
#coding: utf8

"""
project: TornadoServer
create date: 2018/6/19 
__author__ = xiashuangxi
"""

import tornado.ioloop
import tornado.web
import os
import sys
from tornado.options import define, options
from common.url_router import include, url_wrapper


class Application(tornado.web.Application):
    def __init__(self):
        handlers = url_wrapper([
            (r"/users/", include('views.users.users_urls'))
        ])
        # 定义 Tornado 服务器的配置项，如 static/templates 目录位置、debug 级别等
        settings = dict(
            debug=True,
            static_path=os.path.join(os.path.dirname(__file__), "static"),
            template_path=os.path.join(os.path.dirname(__file__), "templates")
        )
        tornado.web.Application.__init__(self, handlers, **settings)


if __name__ == '__main__':
    print("Tornado server is ready for service\r")
    tornado.options.parse_command_line()
    Application().listen(8000, xheaders=True)
    tornado.ioloop.IOLoop.instance().start()


