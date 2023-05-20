import scraper
from colorama import Fore


user_valute_name = ' '
desired_valute_name = ' '
user_valute_amount = 0
user_valute = None
desired_valute = None


def list_currencies():
    welcome_msg = "Доступні валюти: "
    for x in scraper.valutes:
        welcome_msg += "\'" + x + "\',"
    print(Fore.YELLOW, welcome_msg)


def gather_user_input():
    global user_valute_name
    user_valute_name = input(Fore.GREEN + "Виберіть вашу валюту: ")
    global desired_valute_name
    desired_valute_name = input(Fore.GREEN + "Виберіть бажану бажаної валюти: ")
    global user_valute_amount
    user_valute_amount = input(Fore.GREEN + "Виберіть кількість вашої валюти: ")


def process_user_input():
    global user_valute
    global desired_valute
    global user_valute_amount

    for x in scraper.valutes:
        if x == user_valute_name:
            user_valute = x
    for x in scraper.valutes:
        if x == desired_valute_name:
            desired_valute = x
    if user_valute is None:
        print(Fore.RED + "Неправильне введення вашої валюти")
        restart()
    if desired_valute is None:
        print(Fore.RED + "Неправильне введення бажаної валюти")
        restart()
    if user_valute_amount.isdigit() is False:
        print(Fore.RED + "Неправильне введення кількості вашої валюти")
        restart()
    print(Fore.BLUE + user_valute_amount + ' ' + user_valute)


def calculate():
    result_amount = \
        float(user_valute_amount) / float(scraper.valutes.get(user_valute)) * float(scraper.valutes.get(desired_valute))
    print(Fore.BLUE, str(round(result_amount, 2)) + " " + desired_valute)


def restart():
    global user_valute
    global desired_valute
    user_valute = None
    desired_valute = None
    list_currencies()
    gather_user_input()
    process_user_input()
    calculate()


restart()
