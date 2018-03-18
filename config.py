from collections import namedtuple

TOKEN = '576701434:AAFxQLWEp4HqxaTvNXFLoS4NHMl6jHrZlmA'
DB = 'd1l38h8lqhilvc'
SERVER = 'ec2-54-221-212-15.compute-1.amazonaws.com'
USER = 'gziqyxvqktbptx'
field = namedtuple('reg', ('name', 'translate'))

user = {
    'url_foto': '',
    'name': '',
    'login': '',
    'info': ''
}

reg = [
    field('url_foto', "ссылку на фото"),
    field('name', "имя"),
    field('info', "о себе"),
    field('pass', 'Конец регистрации')
]

users_reg_id = {}
users_info = {}
