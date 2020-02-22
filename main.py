# -*- coding: UTF-8 -*-
print("Blessing Skin 批量导入")

print("输入Mysql地址:")
address=input()
print("输入Mysql用户名")
username=input()
print("输入Mysql密码")
passwd=input()
print("输入Mysql表名称")
tablename=input()
print("输入需导入的文件夹")
file=input()
print("输入目标文件夹")
Tofile=input()
print("皮肤格式")
skin_type=input()
'''
address = "*****"
username = "****"
passwd = "******"
tablename = "****"
file = "./****/"
Tofile = "/www/****/storage/textures/"
'''
import os
import hashlib
import pymysql
import shutil
pymysql.install_as_MySQLdb()

try:
    db = pymysql.connect(address, username, passwd, tablename, charset='utf8' )
    t_file=os.listdir(file)
    for i in t_file:
        path = file+i
        with open(path,'rb') as i2:
            sha256 = hashlib.sha256(i2.read()).hexdigest()
            #print(sha256)
            (name, extension) = os.path.splitext(i)
            #print(name)
            sql = "INSERT INTO `textures` (`name`, `type`, `hash`, `size`, `uploader`, `public`, `upload_at`, `likes`) VALUES ( '{0}', '{1}', '{2}', '{3}', '{4}', '{5}', '{6}', '0')".format(name,skin_type,sha256,2,1,1,"2020-02-12 12:15:51")
            shutil.copyfile(path,Tofile+sha256)
            try:
                cursor = db.cursor()
                cursor.execute(sql)
                db.commit()
                print("成功")
            except:
                db.rollback()
                print("失败")
    db.close()
except BaseException as e:
    print(e)
