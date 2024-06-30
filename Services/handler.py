import os
import sys

def listen(inputString):
    from UI.ui import Main
    from Services.parse import parseString
    
    try:
        if inputString == "1":
            Main.inputUI()
        elif inputString == "2":
            Main.historyUI("")
        elif inputString.lower() == "назад":
            Main.mainUI()
        elif inputString == "3":
            sys.exit()
        elif os.path.isfile(inputString):
            parseString(inputString)
        else:
            Main.mainUI()
    except KeyboardInterrupt:
        os.system("cls")
        sys.exit(1)
