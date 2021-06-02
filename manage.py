from flask import Flask
from flask_sqlalchemy import SQLAlchemy

class Config(object):
	'''项目的配置（自定义）'''
	DEBUG=True

	# 为 数据库 添加配置
	SQLALCHEMY_DATABASE_URI="mysql://root:mysql@127.0.0.1:3306/information27"
	SQLALCHEMY_TRACK_MODIFICATIONS=False
app = Flask(__name__)

# 加载配置
app.config.from_object(Config)

db=SQLAlchemy(app)



@app.route('/')
def index():
	return 'index222'


if __name__ == '__main__':
	app.run()