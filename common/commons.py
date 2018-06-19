#!/usr/bin/env python
#coding: utf8

"""
project: TornadoServer
create date: 2018/6/19 
__author__ = xiashuangxi
"""

import json


def http_response(self, msg, code):
    self.write(json.dumps({"data": {"msg": msg, "code": code}}))


if __name__ == "__main__":
    http_response()
