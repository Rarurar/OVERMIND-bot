from colorama import Fore
import sys
import datetime
import re
import Themes


class LoggerOut(object):
    def __init__(self):
        self.terminal = sys.stdout
        t = str(datetime.datetime.now().strftime("(%Y-%m-%d %H.%M.%S)"))
        self.log = open(f"Діалог{t}.txt", "w+", encoding='utf-8')

    def write(self, message):
        self.terminal.write(message)
        self.log.write(re.sub('\033\[[^m]*m', '', message)+'\n')

    def flush(self):
        pass


sys.stdout = LoggerOut()


print(Fore.YELLOW + "Привіт, мене звати Overmind!")


Themes.Bot()
