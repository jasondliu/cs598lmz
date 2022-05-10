import codecs
codecs.register(lambda name: codecs.lookup('utf8') if name == 'utf8mb4' else None)
# import pymysql
# pymysql.install_as_MySQLdb()

# from django.db import models

# class MyModel(models.Model):
#     ...
#     class Meta:
#         db_table = 'my_table'

# class MyModel(models.Model):
#     ...
#     class Meta:
#         db_table = 'my_table'
#         managed = False

# class MyModel(models.Model):
#     ...
#     class Meta:
#         db_table = 'my_table'
#         managed = False
#         db_tablespace = 'mysql'

# class MyModel(models.Model):
#     ...
#     class Meta:
#         db_table = 'my_table'
#         managed = False
#         db_tablespace = 'mysql'
#         db_tablespace_suffix = '_suffix'

#
