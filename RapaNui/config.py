#encoding:utf-8

#开发环境配置
DEBUG = True

SQLALCHEMY_TRACK_MODIFICATIONS = True
SECRET_KEY = "A0Zr98j/3yX R~XHH!jmN]LWX/,?RT"

#数据库配置
HOSTNAME = '127.0.0.1'
PORT     = '3306'
DATABASE = 'RapaNui'
USERNAME = 'root'
PASSWORD = 'root'
DB_URI = 'mysql://{}:{}@{}/{}'.format(USERNAME, PASSWORD, HOSTNAME, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URI