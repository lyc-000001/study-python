import sqlalchemy
from datetime import datetime
from sqlalchemy import Column, Integer, String, create_engine, DateTime
from sqlalchemy.ext.declarative import declarative_base
from db_link_test import engine, session

Base = sqlalchemy.orm.declarative_base()


class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, nullable=False, primary_key=True)
    user_name = Column(String(100), nullable=False, comment='用户名')
    user_password = Column(String(100), nullable=False, comment='密码')
    nick_name = Column(String(100), comment='昵称')
    roles = Column(String(255), nullable=False, comment='权限')
    create_time = Column(DateTime, nullable=False, default=datetime.now, comment='创建时间')
    update_time = Column(DateTime, nullable=False, default=datetime.now, onupdate=datetime.now, comment='更新时间')


# 创建表
# Base.metadata.create_all(engine)
# new_user = User(name='Alice', age=25)
# session.add(new_user)
# session.commit()
# session.close()

# users = session.query(User).all()
# for user in users:
#     print(user.name, user.age)
