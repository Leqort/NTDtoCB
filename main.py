import os
import sys


def main():
    try:
        from Services.crash import criticalError
        from Services.handler import listen
        from Services.parse import parseString
        from UI.ui import Main

        Main.mainUI()
    except ImportError as err:
        criticalError("ImportError!", err)
        sys.exit(1)


if __name__ == "__main__":
    main()
