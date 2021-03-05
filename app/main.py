#!/usr/bin/env python3

from sqlalchemy import create_engine, event
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey, Boolean
from sqlalchemy.dialects.postgresql import JSON, JSONB, TSVECTOR
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

from os import environ

# In docker-compose, DATABASE_URL will point to postgres
url = environ.get('DATABASE_URL', 'sqlite:///:memory:')
engine = create_engine(url, echo=True)

Base = declarative_base()
metadata = Base.metadata

class User(Base):
    __tablename__ = 'user'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    active = Column(Boolean)
    fullname = Column(String)
    nickname = Column(String)
    vec1 = Column(TSVECTOR)
    vec2 = Column(TSVECTOR)
    test = Column(String)
    data = Column(JSON)
    datab = Column(JSONB)
#    group_id = Column(Integer, ForeignKey('Group.id'))

#    group = relationship('Group', primaryjoin='foreign(User.group_id) == Group.id')
#    group = relationship('Group', back_populates='users')
    groups = relationship('Group', secondary='user_group')
    #, foreign_keys='[UserGroup.user_id, UserGroup.group_id]')

@event.listens_for(User.fullname, 'set')
def fullname_set(target, value, oldvalue, initiator):
    print(target, value, oldvalue, initiator)
    import pdb;pdb.set_trace()

#@event.listens_for(User, 'after_flush')
#def user_flushed(**kwargs):
#  print(kwargs)
#  import pdb;pdb.set_trace()

'''
users = Table('users', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('active', Boolean),
    Column('fullname', String),
)
'''

class Group(Base):
    __tablename__ = 'group'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    active = Column(Boolean)

#    users = relationship('User', back_populates='group')
    users = relationship('User', secondary='user_group')
    #, foreign_keys='[UserGroup.user_id, UserGroup.group_id]')

class UserGroup(Base):
    __tablename__ = 'user_group'
    user_id = Column(Integer, ForeignKey(User.id), primary_key=True)
    group_id = Column(Integer, ForeignKey(Group.id), primary_key=True)


metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)
session = Session()

#print(str(session.query(User).filter(Group.active)))
x = session.query(User).filter_by(active=True).with_for_update(nowait=True)
import pdb;pdb.set_trace()


