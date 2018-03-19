from collections import namedtuple

TOKEN = '576701434:AAFxQLWEp4HqxaTvNXFLoS4NHMl6jHrZlmA'
DB = 'd1l38h8lqhilvc'
SERVER = 'ec2-54-221-212-15.compute-1.amazonaws.com'
USER = 'gziqyxvqktbptx'
field = namedtuple('reg', ('name', 'translate', 'func', 'ars'))
field.__new__.__defaults__ = (None,) * 4
user = {
    'url_foto': '',
    'name': '',
    'login': '',
    'info': ''
}

reg = [
    field('url_foto', "[1/9] Фото: Отправь фото прямо сюда. Пользователи должны знать, как ты выглядишь."),
    field('name', "Отлично!|[2/9] Имя: Как тебя представить другим пользователям?  Напиши сюда свое имя."),
    field('info', "Приятно познакомиться {})|[3/9] Город: В каком городе ты живешь или часто бываешь? "
                  "Выбери из списка, ты сможешь изменить его в любой момент в своем профиле.", None, ('name',)),
    field('citec', "Тестовая строка"),
    field('pass', 'Конец регистрации')
]

users_reg_id = {}
users_info = {}
