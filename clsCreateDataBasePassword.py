from os import urandom
from hashlib import pbkdf2_hmac


class CreateDataBasePassword:
    def __init__(self):
        pass

    def set_first_pass(self, password):
        self.__salt = urandom(32)
        self.__key = pbkdf2_hmac('md5', password.encode(), self.__salt, 100000)
        return {'Salt': str(self.__salt), 'Key': str(self.__key)}

    def get_salt(self):
        return self.__salt.decode('ISO-8859-1')

    def get_key(self):
        return self.__key.decode('ISO-8859-1')
