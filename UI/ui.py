import os
from UI.logo import logo
from Services.handler import listen

class Main():
    def mainUI():
        os.system("cls")
        
        logo()
        transfer = input("""                         MAIN
              1. Перевод файла в кб стиль
              2. История
              3. Выход
              
              Пользовательский ввод: """)
        listen(transfer)
        
        
        
    def inputUI():
        os.system("cls")
        
        logo()
        transfer = input("""                         Input
              Введите путь к файлу(Пример: D:/Downloads/new.pwn)
              Или напишите "Назад", для возврата в меню.

              Пользовательский ввод: """)
        listen(transfer)
        
        
    def resultUI(result):
        os.system("cls")
        
        logo()
        transfer = input(f"""                         Result
              {result}
              Для возврата в меню, напишите "Назад".

              Пользовательский ввод: """)
        listen(transfer)
        
    def historyUI(history):
        os.system("cls")
        
        history = ""
        
        logo()
        
        transfer = input(f"""                         History
              {history}
              01.01.1970 00:00 0 450 650 250 250 0 14 15 0xFFFFTEXT 0xFFFFTEXT 1 0 2 0 -1 255
              01.01.1970 00:01 0 450 650 250 250 0xFFBBOOXX 2 1 19315 15 25 36 1.0 0x000MODEL 0x000MODEL 0 -1

              Для возврата в меню, напишите "Назад".

              Пользовательский ввод: """)
        listen(transfer)        