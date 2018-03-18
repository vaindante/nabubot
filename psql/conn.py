from peewee import PostgresqlDatabase

from config import USER, SERVER, DB

psql_db = PostgresqlDatabase(
    DB,
    user=USER,
    password='0ffe9bb3a52776fd372981a01b4dec1c458ded86f2c6f2cb1dff42128aba601b',
    host=SERVER,
    port=5432
)
