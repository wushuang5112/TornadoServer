#!/usr/bin/env python
#coding: utf8

"""
project: TornadoServer
create date: 2018/6/19 
__author__ = xiashuangxi
"""


import os
import json


def http_response(self, msg, code):
    self.write(json.dumps({"data": {"msg": msg, "code": code}}))


def save_files(file_metas, in_rel_path, type='image'):
    """
    Save file stream to server
    """
    file_path = ""
    file_name_list = []
    for meta in file_metas:
        file_name = meta['filename']
        file_path = os.path.join( in_rel_path, file_name )
        file_name_list.append( file_name )
        #save image as binary
        with open( file_path, 'wb' ) as up:
            up.write( meta['body'] )
    return file_name_list


if __name__ == "__main__":
    http_response()
