import sys
from bank_db import *

name_passed = False
surname_passed = False
card_number_passed = False
name = None
surname = None


def registration():
    global name_passed
    global surname_passed
    global card_number_passed
    global name
    global surname

    if not name_passed:
        input_name = input("Write name: ")
        if input_name.isalpha() and len(input_name) > 2:
            name_passed = True
            name = input_name
        else:
            print("Write valid name")
            registration()
    if not surname_passed:
        input_surname = input("Write surname: ")
        if input_surname.isalpha() and len(input_surname) > 5:
            surname_passed = True
            surname = input_surname
        else:
            print("Write valid surname")
            registration()

    if not card_number_passed:
        repeted = False
        card_number = input("Write card number: ")
        if len(card_number) == 12 and card_number.isdigit():
            lst = get_all_users_card_number()
            if card_number in lst:
                print("arden ka")
                repeted = True
                registration()
            if repeted == False:
                create_user(name, surname, card_number, 0)


        else:
            print("Write valid card_number")
            registration()


def check_balance():
    card_number=input(" Write card number : ")
    mon=get_money_from_card_number(card_number)
    if mon==-1:
        print("Write valid card number")
        check_balance()
    else:
        print(mon)




def add_balance():
    card_number = input(" Write card number : ")
    money=input("How much you want add : ")
    if money.isdigit():
        if int(money)>0:
            update_balance(card_number,money)
    else:
        print("write valid money")



def transfer_money():
    card_number_from=input("Write card number where do you want to trasfer from  : ")
    card_number_to=input("Write card number where do you want forward : ")
    money = input("How much you want add : ")
    if money.isdigit():
        if int(money) > 0:
            transfer_balance(card_number_from,card_number_to,money)
    else:
        print("write valid money")

def show_users():
    pass


def show_users_by_balance():
    pass


def delete_account():
    pass


print(
    "Options: Reg | Check Balance | Add Balance | Transfer Money | Show Users | Show Users By Balance | Delete Account | Exit")
while True:
    option = input("> ")
    if option == "Reg":
        registration()
    elif option == "Check Balance":
        check_balance()
    elif option == "Add Balance":
        add_balance()
    elif option == "Transfer Money":
        transfer_money()
    elif option == "Show Users":
        show_users()
    elif option == "Show Users By Balance":
        show_users_by_balance()
    elif option == "Delete Account":
        delete_account()
    elif option == "Exit":
        sys.exit()
    else:
        print("is not an option")
