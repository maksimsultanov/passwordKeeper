class SaveSalt:
    def __init__(self):
        pass

    @staticmethod
    def create_salt_file(salt):
        with open('salt', 'w+') as f:
            f.write(salt)


if __name__ == '__main__':
    pass
