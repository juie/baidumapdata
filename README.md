# baidumapdata
可以根据自定义关键词获取地理位置数据，包括名称、详细地址、联系电话、经纬度、街道编号等，需调用百度地图API，基于mongoDB和mapapi。
###步骤
`pip install pymongo`

`pip install mapapi`

`python baidumapdata.py`

###mongoDB导出数据库文件为csv格式的用法

在shell命令行执行

`/usr/bin/mongoexport -u 用户名 -p 密码 -d 数据库名称 -c 表名称 --csv -f name,address,telephone,location,street_id,uid,_id -o csv名称.dat`
