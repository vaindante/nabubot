from func.methods import *
from psql.base_model import *
from settings import bot


def create_tables():
    with psql_db:
        psql_db.create_tables([Users, Cites, Tags, AgeUser, Room])


@bot.message_handler(commands=['start'])
def add_user(msg):
    is_registration(bot, msg, Users, start=1)


@bot.message_handler(commands=['find_user'])
def find_user(msg):
    # tmp = msg.text.split()[1]
    # bot.send_message(msg.chat.id, Users.select().where(tmp in Users.name).get())
    pass


@bot.message_handler()
def get_msg(msg):
    is_registration(bot, msg, Users)


if __name__ == '__main__':
    create_tables()
    log.info('test')
    bot.polling(none_stop=True)
