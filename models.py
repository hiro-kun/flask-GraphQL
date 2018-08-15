from sqlalchemy import *
from sqlalchemy.orm import (scoped_session, sessionmaker, relationship,
                            backref)
from sqlalchemy.ext.declarative import declarative_base

import pymysql
pymysql.install_as_MySQLdb()

DATABASE = 'mysql://%s:%s@%s/%s?charset=ujis' % (
    "root",
    "",
    "127.0.0.1",
    "sample",
)

ENGINE = create_engine(
    DATABASE,
    # encoding="euc-jp",
    echo=True  # Trueだと実行のたびにSQLが出力される
)

# Sessionの作成
db_session = scoped_session(
    sessionmaker(
        autocommit=False,
        autoflush=False,
        bind=ENGINE
    )
)

Base = declarative_base()
# We will need this for querying
Base.query = db_session.query_property()


'''
テーブル定義
'''
class DepartmentRef(Base):
    __tablename__ = 'department_ref'
    id = Column(Integer, primary_key=True)
    department_name = Column(String)
    staff_id = Column(Integer,ForeignKey('staff.id'))

class Staff(Base):
    __tablename__ = 'staff'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    branch = Column(String)
    age = Column(String)

    department = relationship(
        DepartmentRef,
        uselist=False,
        backref='staff'
    )
     