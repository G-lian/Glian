# 数据库的配置信息

# mysql所在的主机名
HOSTNAME = "127.0.0.1"
# mysql监听的端口号，默认为3306
PORT = 3306
# mysql上创建的数据库名称
DATABASE = "OA"
# 连接mysql的用户名∏
USERNAME = "root"
# 连接mysql的密码
PASSWORD = "root"

DB_URL = 'mysql+pymysql://{}:{}@{}:{}/{}?charset=utf8mb4'.format(USERNAME, PASSWORD, HOSTNAME, PORT, DATABASE)
SQLALCHEMY_DATABASE_URI = DB_URL


# 邮箱配置
# gsspgntbuoptdhad
MAIL_SERVER = 'smtp.qq.com'
MAIL_USE_SSL = True
MAIL_PORT = 465
MAIL_USERNAME = '3133185472@qq.com'
MAIL_PASSWORD = 'gsspgntbuoptdhad'
MAIL_DEFAULT_SENDER = '3133185472@qq.com'
