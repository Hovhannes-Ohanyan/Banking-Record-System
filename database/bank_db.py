"""This file create db and table and is connected with sql"""

import sqlite3

conn = sqlite3.connect("../database/bank_recording.db")
cursor = conn.cursor()
cursor.execute('''
          CREATE TABLE IF NOT EXISTS bank_users(
                name text,
                surname text,
                card_number text,
                money int
          ) ''')


def create_user(name, surname, card_number, money):
    """This function is creates user"""

    connection = sqlite3.connect('../database/bank_recording.db')
    cur = connection.cursor()
    with connection:
        cur.execute("INSERT INTO bank_users VALUES (:name, :surname, :card_number, :money)",
                    {'name': name, 'surname': surname,
                     'card_number': card_number, 'money': money})


def get_money_from_card_number(card_number):
    """This function return user's balance"""

    con = sqlite3.connect('../database/bank_recording.db')
    cur = con.cursor()
    with con:
        cur.execute("SELECT * FROM bank_users")
        data = cur.fetchall()
        lst = []
        for dat in data:
            lst.append(dat)
        for element in lst:
            if element[2] == card_number:
                return element[3]
        return -1


def get_surname_from_name(name):
    """This function return list of user's surname"""
    con = sqlite3.connect('../database/bank_recording.db')
    cur = con.cursor()
    with con:
        cur.execute("SELECT * FROM bank_users")
        data = cur.fetchall()
        lst = []
        lst_surnames = []
        for dat in data:
            lst.append(dat)
        for element in lst:
            if element[0] == name:
                lst_surnames.append(element[1])
        return lst_surnames


def get_card_number_from_name_surname(name, surname=None):
    """This function is return card number by name and surname"""
    con = sqlite3.connect('../database/bank_recording.db')
    cur = con.cursor()
    with con:
        cur.execute("SELECT * FROM bank_users")
        data = cur.fetchall()
        lst = []
        for dat in data:
            lst.append(dat)
        for element in lst:
            if element[0] == name and surname is None:
                return element[2]
            elif element[0] == name and element[1] == surname:
                return element[2]


def get_all_users_card_number():
    """This function return user's balance"""

    con = sqlite3.connect('../database/bank_recording.db')
    cur = con.cursor()
    with con:
        cur.execute("SELECT * FROM bank_users")
        data = cur.fetchall()
        lst = []
        for cont in data:
            lst.append(cont[2])
        return lst



def update_balance(card_number, money):
    """ This function is updates money from card number"""
    if card_number in get_all_users_card_number():
        balance = get_money_from_card_number(card_number)
        money = int(balance) + int(money)
        con = sqlite3.connect('../database/bank_recording.db')
        cur = con.cursor()
        with con:
            cur.execute("UPDATE bank_users SET money=:money WHERE card_number=:card_number",
                        {'money': str(money), 'card_number': card_number})

    else:
        print("Write valid card number and enter Update Balance option again")


def transfer_balance(card_number_from, card_number_to, money):
    """This function is transfer money from one account to another"""
    if (card_number_from and card_number_to) in get_all_users_card_number():
        if get_money_from_card_number(card_number_from) >= int(money):
            update_balance(card_number_to, money)
            update_balance(card_number_from, f'-{money}')
            print("Done")
        else:
            print("There is not enough money ")

    else:
        print("Write valid card numbers and enter the Transfer Money option again")


def show_all_users():
    """This function is returns all users"""
    con = sqlite3.connect('../database/bank_recording.db')
    cur = con.cursor()
    with con:
        cur.execute("SELECT * FROM bank_users")
        users = cur.fetchall()
        lst = []
        for user in users:
            lst.append(user)
        return lst


def show_users_sort_by_balance():
    """This function is returns all users,but sorted by balance"""
    con = sqlite3.connect('../database/bank_recording.db')
    cur = con.cursor()
    with con:
        cur.execute("SELECT * FROM bank_users  ORDER BY money")
        users = cur.fetchall()
        lst = []
        for user in users:
            lst.append(user)
        return lst


def delete_user(card_number):
    """This function delete user"""

    connection = sqlite3.connect('../database/bank_recording.db')
    cur = connection.cursor()
    with connection:
        cur.execute("DELETE from bank_users WHERE card_number = :card_number",
                    {'card_number': card_number})


conn.commit()
conn.close()
