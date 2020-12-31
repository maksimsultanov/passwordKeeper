from os.path import exists


class DBConnect:
    def __init__(self):
        pass

    def check_db(self, db_name):
        return exists(db_name)

    def create_db(self, db_name):
        if not self.check_db(db_name):
            pass
