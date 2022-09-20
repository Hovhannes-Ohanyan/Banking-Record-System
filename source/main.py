"""This file is head file"""
import sys
from database.bank_db import create_user, get_money_from_card_number, update_balance, \
    transfer_balance, show_all_users, delete_user, get_card_number_from_name_surname, \
    get_surname_from_name, show_users_sort_by_balance, get_all_users_card_number


def inputName():
    """This function is for input name"""
    name = input("Write your name : ")
    if name.lower() == 'cancel' :
        return main()
    if name.isalpha() and len(name) > 2:
        return name
    print("Write valid name")
    return inputName()


def inputSurname():
    """This function is for input surname"""
    surname = input("Write your surname : ")
    if surname.lower() == 'cancel' :
        main()
    if surname.isalpha() and len(surname) > 5:
        return surname
    print("Write valid surname")
    return inputSurname()


def inputCardNumber():
    """This function is for input card number"""
    card_number = input("Write your card number : ")
    if card_number.lower() == 'cancel':
        main()
    if card_number.isdigit() and len(card_number) == 12:
        lst_cards = get_all_users_card_number()
        if card_number not in lst_cards:
            return card_number
        elif card_number in lst_cards:
            print("Already exist!")
            return inputCardNumber()
    else:
        print("Write valid card number")
        return inputCardNumber()


def registration():
    """This function is for registration users"""
    name = inputName()
    surname = inputSurname()
    card_number = inputCardNumber()
    create_user(name, surname, card_number, 0)
    print("Successfully created")


def checkBalance():
    """This function is for seeing users balance"""
    card_number = input('Enter card number: ')
    if card_number.lower() == 'cancel':
        return main()
    if card_number.isdigit() and len(card_number) == 12 \
            and card_number in get_all_users_card_number():
        mon = get_money_from_card_number(card_number)
        if mon == -1:
            print("Card not found")
        else:
            print(f"Your balance is : {get_money_from_card_number(card_number)}")
    else:
        print("Write valid card number")
        return checkBalance()


def addBalance():
    """This function is for add balance"""
    card_number = input('Enter card number: ')
    if card_number.lower() == 'cancel':
        return main()
    if card_number.isdigit() and len(card_number) == 12 \
            and card_number in get_all_users_card_number():
        money = input("How much you want add : ")
        if money.isdigit():
            if int(money) > 0:
                update_balance(card_number, money)
                print("Balance added")
        else:
            print("write valid money and enter the Add Balance option again")
    else:
        print("valid card number")
        return addBalance()


def transferMoney():
    """This function is for transfer money"""
    cards = get_all_users_card_number()
    card_number_from = input("Write card number where do you want to trasfer from  : ")
    if card_number_from.lower() == 'cancel':
        return main()
    if card_number_from not in cards:
        print("Card doesn't Valid")
        return transferMoney()

    card_number_to = input("Write card number where do you want forward : ")
    if card_number_to.lower() == 'cancel':
        return main()
    if card_number_to not in cards:
        print("Card doesn't Valid")
        return transferMoney()

    money = input("How much you want add : ")
    if money.isdigit() and int(money) > 0:
        transfer_balance(card_number_from, card_number_to, money)
    else:
        print("write valid money and enter the Transfer Money option again")


def showUsers():
    """This function is for show all users"""
    data = show_all_users()
    if len(data) == 0:
        print("There is no users")
        return
    for element in data:
        print(element[0], element[1], element[2], f'{element[3]}' + ".00amd", end="\n")


def showUsersByBalance():
    """This function is for show  sorted users by balance"""
    data = show_users_sort_by_balance()
    if len(data) == 0:
        print("There is no users")
        return
    for element in data:
        print(element[0], element[1], element[2], f'{element[3]}' + ".00amd", end="\n")


def deleteAccount():
    """This function is deletes account"""
    name = inputName()
    lst_name = []
    users = show_all_users()
    for element in users:
        lst_name.append(element[0])

    if name not in lst_name:
        print(" User not found")
        return deleteAccount()

    if lst_name.count(name) == 1:
        delete_user(get_card_number_from_name_surname(name))
        print("Account deleted")

    elif lst_name.count(name) > 1:
        lst_surname = get_surname_from_name(name)
        print("Select your surname")
        for surname in lst_surname:
            print(surname)
        surname = inputSurname()

        if surname in lst_surname:
            if lst_surname.count(surname) > 1:
                card_number = input("Write card number : ")
                if len(card_number) == 12 and card_number.isdigit() and card_number in get_all_users_card_number():
                    delete_user(card_number)
                    print("Account deleted")
                    return
        else:
            print("Write valid surname")
            return deleteAccount()

        if surname in lst_surname:
            card_num = get_card_number_from_name_surname(name, surname)
            delete_user(card_num)
            print("Account deleted")
        else:
            print(f"{surname} {name} user don't exict")


def main():
    while True:
        print(
            "Options: Registration | Check balance | Add balance | Transfer money | "
            "Show users | Show users by balance | Delete account | Exit")
        option = input("> ")
        option = option.lower()
        if option == "registration":
            registration()
        elif option == "check balance":
            checkBalance()
        elif option == "add balance":
            addBalance()
        elif option == "transfer money":
            transferMoney()
        elif option == "show users":
            showUsers()
        elif option == "show users by balance":
            showUsersByBalance()
        elif option == "delete account":
            deleteAccount()
        elif option == "exit":
            sys.exit()
        else:
            print("Is not an option")


main()
