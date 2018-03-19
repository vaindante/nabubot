from config import reg, users_reg_id, users_info, user
from settings import log
import time


def _paste_to_user(key, value):
    log.debug(f'{users_info[value.chat.id][key]} - {value.text}')
    users_info[value.chat.id][key] = value.text


def create_user(user_model, **kwargs):
    return user_model.create(**kwargs)


def add(model, **kwargs):
    return model.create(**kwargs)


def select(model, name, params):
    try:
        return model.select().where(params == getattr(model, name)).get()
    except:
        return None


def is_registration(bot, msg, users_model, start=None):
    tst = select(users_model, 'login', msg.chat.id)
    log.info(f'{msg.chat.id} - {tst}')
    if tst is None:
        if start:
            users_reg_id[msg.chat.id] = 0
            users_info[msg.chat.id] = user.copy()
            bot.send_message(msg.chat.id, 'Заполните, пожалуйста, ваш профиль:').wait()
            # TODO: await?
            # time.sleep(.2)
            bot.send_message(msg.chat.id, reg[users_reg_id[msg.chat.id]].translate)
        if not start:
            registration(bot, msg, users_model)
    else:
        bot.send_message(msg.chat.id, 'Добро пожаловать:)')


def __add_msg(_reg, t, _user):
    log.info(_reg)
    if _reg.ars:
        return t.format(*[_user[v] for v in _reg.ars])
    return t


def registration(bot, msg, users_model):
    if users_reg_id[msg.chat.id] + 1 <= len(reg):
        _paste_to_user(reg[users_reg_id[msg.chat.id]].name, msg)
        users_reg_id[msg.chat.id] += 1
        for t in reg[users_reg_id[msg.chat.id]].translate.split('|'):
            bot.send_message(
                msg.chat.id,
                __add_msg(reg[users_reg_id[msg.chat.id]], t, users_info[msg.chat.id])
            ).wait()
        log.info(users_reg_id[msg.chat.id])

    if reg[users_reg_id[msg.chat.id]].name == 'pass':
        users_info[msg.chat.id]['login'] = msg.chat.id
        users_model.create(**users_info[msg.chat.id])
        log.info(users_info[msg.chat.id])
