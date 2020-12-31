# from clsPassCreator import PassCreator
# from json import loads

"""TkInter TodoList
    Python 3.7"""
import tkinter.messagebox
from clsCreateDataBasePassword import CreateDataBasePassword
from clsPassKeeper import PassKeeper
from clsSaveSalt import SaveSalt


def main_def():
    # print("start pass keeping")
    # print("Enter user name")
    # uname = input()
    # print("Enter password")
    # upass = input()
    # print("Create user...")
    # user = PassCreator(uname, upass)
    # print(user.getname())
    # print(user.getsalt())
    # print(user.getkey().encode('ISO-8859-1'))
    # full = user.getname() + user.getsalt() + user.getkey()
    # print(full)
    #
    # # print(user.get_as_json())
    # # js_nuser = loads(user.get_as_json())
    # # nuser = PassCreator(js_nuser['User'], )
    # # print(nuser.get_as_json())
    #
    # print("enter user name and password")
    # s_pass = input()
    # s_pass = s_pass.split()
    # s_user = s_pass[0]
    # s_password = s_pass[1]
    # print(user.check_password(s_user, s_password))

    newpass = CreateDataBasePassword()
    newpass.set_first_pass('mypassword')
    # print(newpass.get_salt())
    print(newpass.get_key())
    SaveSalt.create_salt_file(newpass.get_salt())


def create_window():
    # Create root window
    root = tkinter.Tk()

    # create a root object
    tdf = PassKeeper(root)

    # Start the main events loop
    root.mainloop()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # main_def()
    create_window()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
