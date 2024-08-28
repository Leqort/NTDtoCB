import os
from UI.logo import logo
from Services.handler import listen


class Main():
    def mainUI():
        os.system("cls")

        logo()
        transfer = input("""                         MAIN
              1. Перевод файла в кб стиль
              2. Выход

              Пользовательский ввод: """)
        listen(transfer, 0)

    def inputUI():
        os.system("cls")

        logo()
        transfer = input("""                         Input
              Введите путь к файлу(Пример: D:/Downloads/new.pwn)
              Или напишите "Назад", для возврата в меню.

              Пользовательский ввод: """)
        listen(transfer, 1)

    def resultUI(result):
        os.system("cls")

        logo()
        transfer = input(f"""                         Result
              {result}
              Для возврата в меню, напишите "Назад".

              Пользовательский ввод: """)
        listen(transfer, 2)
