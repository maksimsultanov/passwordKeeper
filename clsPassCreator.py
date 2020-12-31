from os import urandom
from hashlib import pbkdf2_hmac
from json import dumps


class PassCreator:
    def __init__(self, userName, userPassword):
        self.__userName = userName
        self.__salt = urandom(16)
        self.__key = pbkdf2_hmac('md5', userPassword.encode('utf-8'), self.__salt, 100000)

    # def __int__(self, userData):
    #     password_and_user = loads(userData)
    #     self.__userName = password_and_user['User']
    #     self.__salt = password_and_user['Salt']
    #     self.__key = password_and_user['Key']

    def getsalt(self):
        return self.__salt.decode('ISO-8859-1')

    def getkey(self):
        return self.__key.decode('ISO-8859-1')

    def getname(self):
        return str(self.__userName)

    def check_password(self, userName, userPassword):
        key = pbkdf2_hmac('md5', userPassword.encode('utf-8'), self.__salt, 100000)
        return self.__key == key and userName == self.__userName

    def get_as_json(self):
        s = self.__salt.decode('ISO-8859-1')
        k = self.__key.decode('ISO-8859-1')
        password_and_user = {'User': str(self.__userName), 'Key': k, 'Salt': s}
        return dumps(password_and_user)


if __name__ == '__main__':
    print("run main.py")
