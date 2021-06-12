from flask_wtf import CSRFProtect
from redis import StrictRedis
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

class Config(object):
	'''项目的配置（自定义）'''
	DEBUG=True

	# 为 数据库 添加配置
	SQLALCHEMY_DATABASE_URI="mysql://root:mysql@127.0.0.1:3306/information27"
	SQLALCHEMY_TRACK_MODIFICATIONS=False

	# Redis的配置
	REDIS_HOST="127.0.0.1"
	REDIS_PORT=6379


app = Flask(__name__)

# 加载配置
app.config.from_object(Config)

# 初始化 数据库
db=SQLAlchemy(app)

# 初始化 redis 存储对象
redis_store=StrictRedis(host=Config.REDIS_HOST,port=Config.REDIS_PORT)
# 开启当前项目 CSRF 保护（因为项目不使用WTF表单，故需要手动配置CSRF）
# 只做服务器的验证功能
CSRFProtect(app)


@app.route('/')
def index():
	return 'index'


if __name__ == '__main__':
	app.run()