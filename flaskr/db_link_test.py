# coding: utf-8
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from tool import read_yaml

# 替换为你的MySQL数据库信息
username = read_yaml('../config/db_config.yaml').get('name')
password = read_yaml('../config/db_config.yaml').get('pwd')
host = read_yaml('../config/db_config.yaml').get('host')  # 例如：'localhost' 或 '127.0.0.1'
port = read_yaml('../config/db_config.yaml').get('port')  # 通常是 3306
database = read_yaml('../config/db_config.yaml').get('database')

# 创建实例，并连接blog库
engine = create_engine(f'mysql+pymysql://{username}:{password}@{host}:{port}/{database}')
Session = sessionmaker(bind=engine)
session = Session()
# 测试连接
# try:
#     connection = engine.connect()
#     print("Successfully connected to the database")
#     connection.close()
# except Exception as e:
#     print(f"Failed to connect to the database: {e}")
