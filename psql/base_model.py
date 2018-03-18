from datetime import datetime

from peewee import *
from pytz import timezone
from .conn import psql_db


class BaseModel(Model):
    """A base model that will use our Postgresql database"""

    class Meta:
        database = psql_db


class Users(BaseModel):
    user_id = PrimaryKeyField()
    create_date = DateField()
    name = CharField(max_length=20)
    login = CharField(max_length=20)
    status = CharField(max_length=20)
    url_foto = CharField()
    info = TextField()
    search = TextField()
    skill = TextField()
    link = CharField

    @classmethod
    def create(cls, **query):
        return super(Users, cls).create(
            create_date=datetime.now(tz=timezone('Etc/GMT-3')),
            **query
        )

    def __str__(self):
        return f'Name: {self.name} Login: {self.login} ID: {self.user_id}'


class Cites(BaseModel):
    id = PrimaryKeyField(primary_key=True)
    name = CharField(max_length=30)


class AgeUser(BaseModel):
    age_id = PrimaryKeyField(primary_key=True)
    age_group = CharField(max_length=20)


class Room(BaseModel):
    room_id = PrimaryKeyField(primary_key=True)
    login_parent = CharField(max_length=20)
    create_date = DateField()
    title = CharField(max_length=20)
    info_id = IntegerField()
    channel = CharField(max_length=20)


class Tags(BaseModel):
    tag_id = PrimaryKeyField(primary_key=True)
    name = CharField(max_length=50)
    create_date = DateField()
    parent_id = IntegerField()

    def __str__(self):
        return 'Name: {}; Id: {}; Create Date: {}, Parent Id: {}'.format(
            self.name,
            self.tag_id,
            self.create_date,
            self.parent_id
        )


class UserWithCites(BaseModel):
    user_id = ForeignKeyField(Users, backref='relationships', field='user_id')
    cites_id = ForeignKeyField(Cites, backref='related_to', field='id')

    class Meta:
        # `indexes` is a tuple of 2-tuples, where the 2-tuples are
        # a tuple of column names to index and a boolean indicating
        # whether the index is unique or not.
        indexes = (
            # Specify a unique multi-column index on from/to-user.
            (('user_id', 'cites_id'), True),
        )
