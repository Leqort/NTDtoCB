import os
import sys


def listen(inputString, window):
    from UI.ui import Main
    from Services.parse import parseString

    try:
        if inputString == "1" and window != 1:
            Main.inputUI()
        elif inputString.lower() == "назад" != 0:
            Main.mainUI()
        elif inputString == "2":
            sys.exit()
        elif os.path.isfile(inputString) and window == 1:
            parseString(inputString)
        else:
            Main.mainUI()
    except KeyboardInterrupt:
        os.system("cls")
        sys.exit(1)
