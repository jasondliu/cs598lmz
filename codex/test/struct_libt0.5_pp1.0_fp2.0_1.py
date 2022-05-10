import _struct

# класс для представления пользователя
class User(object):

    def __init__(self, user_id, user_name, user_password):
        self.__id = user_id
        self.__name = user_name
        self.__password = user_password

    def get_id(self):
        return self.__id

    def get_name(self):
        return self.__name

    def get_password(self):
        return self.__password

    def set_id(self, id):
        self.__id = id

    def set_name(self, name):
        self.__name = name

    def set_password(self, password):
        self.__password = password

    def __str__(self):
        return 'ID: {0}\nName: {1}\nPassword: {2}'.format(self.__id, self.__name, self.__password)

#
