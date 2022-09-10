import sqlite3

con = sqlite3.connect("bank_recording.db")
cursor = con.cursor()
cursor.execute('''
          CREATE TABLE IF NOT EXISTS bank_users(
                name text,
                surname text,
                card_number text,
                money int
          ) ''')


def create_user(name, surname, card_number, money):
    """This function is creates user"""

    connection = sqlite3.connect('bank_recording.db')
    cursor = connection.cursor()
    with connection:
        cursor.execute("INSERT INTO bank_users VALUES (:name, :surname, :card_number, :money)",
                       {'name': name, 'surname': surname,
                        'card_number': card_number, 'money': money})


def get_all_users_card_number():
    """This function return user's balance"""

    con = sqlite3.connect('bank_recording.db')
    cursor = con.cursor()
    with con:
        cursor.execute("SELECT * FROM bank_users")
        contact = cursor.fetchall()
        lst = []
        for cont in contact:
            lst.append(cont[2])
        return lst

def get_money_from_card_number(card_number):
    """This function return user's balance"""

    con = sqlite3.connect('bank_recording.db')
    cursor = con.cursor()
    with con:
        cursor.execute("SELECT * FROM bank_users")
        contact = cursor.fetchall()
        lst = []
        for cont in contact:
            lst.append(cont)
        for el in lst:
            if el[2]==card_number:
                return el[3]
        return -1

#print(get_all_users_card_number())

def update_balance(card_number,money):
    """ This function is updates money from card number"""
    if card_number in get_all_users_card_number():
        balance=get_money_from_card_number(card_number)
        money = int(balance) + int(money)
        con = sqlite3.connect('bank_recording.db')
        cursor = con.cursor()
        with con:
            cursor.execute("UPDATE bank_users SET money=:money WHERE card_number=:card_number", {'money':str(money),'card_number':card_number})
            print("Done")

    else:
        print("Write valid card number")

def transfer_balance(card_number_from,card_number_to,money):
    """This function is transfer money from one account to another"""
    if (card_number_from and card_number_to) in get_all_users_card_number():
        if get_money_from_card_number(card_number_from)>=int(money):
            update_balance(card_number_to,money)
            update_balance(card_number_from,f'-{money}')
        else:
            print("There is not enough money")
    else:
        print("Write valid card numbers")

