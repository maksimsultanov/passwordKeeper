from tkinter import Frame, Menu


class PassKeeper(Frame):
    """Main frame pass keeper"""
    def __init__(self, master):
        """Constructor main window"""
        # set the parent as root
        Frame.__init__(self, master=None)
        # add menu to main frame
        self.__create_menu()

    def __create_menu(self):
        """create menu function"""
        # create menu bar
        self.__menu_bar = Menu(self.master)
        self.master.config(menu=self.__menu_bar)
        # create file menu
        self.__file_menu = Menu(self.__menu_bar)
        # add record menu button
        self.__file_menu.add_command(label="Добавить запись в БД...")
        # edit record menu button
        self.__file_menu.add_command(label="Редактировать запись в БД...")
        # delete record menu button
        self.__file_menu.add_command(label="Удалить запись из БД...")
        # create menu button exit
        self.__file_menu.add_command(label="Выход", command=self.__close_app)
        # add file menu to menu bar
        self.__menu_bar.add_cascade(label="Файл", menu=self.__file_menu)
        # create file menu
        self.__database_menu = Menu(self.__menu_bar)
        # create db password menu
        self.__database_menu.add_command(label="Создать пароль для БД...")
        # change db password menu
        self.__database_menu.add_command(label="Создать новый пароль для БД...")
        # set path to key menu
        self.__database_menu.add_command(label="Путь к файлам с ключами...")
        # set path to db menu
        self.__database_menu.add_command(label="Путь к файлу с БД...")
        # add db menu to menu bar
        self.__menu_bar.add_cascade(label="БД", menu=self.__database_menu)
        # create help menu
        self.__help_menu = Menu(self.__menu_bar)
        # help menu button
        self.__help_menu.add_command(label="Справка...")
        # about menu button
        self.__help_menu.add_command(label="О программе")
        # add help menu to menu bar
        self.__menu_bar.add_cascade(label="Помощь", menu=self.__help_menu)

    def __close_app(self):
        """app close function"""
        self.master.destroy()
