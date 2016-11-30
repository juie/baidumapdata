#!/usr/bin/env python
# -*- coding: utf-8 -*-
import json
import pymongo
from mapapi import baidu
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

map_api = baidu.MapApi(['百度地图API Key'])

def dealData():
    keyword=['酒店','公寓','宾馆']
    city=['东莞']
    for i in keyword:
        for j in city:
            ret = map_api.place_api.get_place_all(i,j)
            for data in ret:
                client = pymongo.MongoClient('localhost', 27017)
                client.gzhotelinfo.authenticate('用户名','密码')
                dghotelinfo= client['dghotelinfo']
                dghotel = dghotelinfo['dghotel']
                dghotel.save(data)
if __name__=='__main__':
    dealData()
