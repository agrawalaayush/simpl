import users
import txn
import merchant
import simpl

def init_simpl():
    simpl.init_simpl()

def new_user(name, email, credit_limit):
    return users.add_users(name, email, credit_limit)

def payback(name, amount):
    return users.payback_user(name, amount)

def get_dues(name):
    return users.get_dues_of_user(name)

def users_at_credit_limit():
    return users.get_users_at_credit_limit()

def total_dues():
    return users.total_dues()

def new_merchant(name, discount):
    merchant.add_merchant(name, discount)

def update_merchant(mname, new_discount):
    merchant.update_merchant(mname, new_discount)

def get_discount(name):
    return merchant.get_discount(name)

def new_txn(name, mname, amount):
    return txn.do_txn(name, mname, amount)

def default():
    return "Wrong Inputs"

import sys
if __name__ == "__main__":
    filename = sys.argv[0]
    command = sys.argv[1]
    rest_arguments = sys.argv[2:]
    #print(rest_arguments)
    if command == "init_simpl":
        init_simpl()
    if command  == "new_user":
        if len(rest_arguments) == 3:
            name = rest_arguments[0]
            email = rest_arguments[1]
            credit_limit = float(rest_arguments[2])
            resp = new_user(name, email, credit_limit)
            print(resp)
        else:
            print("Wrong user input")
    elif command == "new_merchant":
        if len(rest_arguments) == 2:
            name = rest_arguments[0]
            discount = float(rest_arguments[1])
            resp = new_merchant(name, discount)
            print(resp)
        else:
            print("Wrong merchant input")
    elif command == "new_txn":
        if len(rest_arguments) == 3:
            name = rest_arguments[0]
            mid = rest_arguments[1]
            amount = float(rest_arguments[2])
            print(new_txn(name, mid, amount))
        else:
            print("Wrong txn input")
    elif command == "update_merchant":
        if len(rest_arguments) == 2:
            mname = rest_arguments[0]
            new_discount = rest_arguments[1]
            resp = update_merchant(mname, new_discount)
            print(resp)
        else:
            print("Wrong input for update merchant")
    elif command == "payback":
        if len(rest_arguments) == 2:
            name = rest_arguments[0]
            amount = float(rest_arguments[1])
            resp = payback(name, amount)
            print(resp)
        else:
            print("Wrong input for payback")
    elif command == "report_discount":
        if len(rest_arguments) == 1:
            mname = rest_arguments[0]
            print(get_discount(mname))
        else:
            print("Wrong input for report discount")
    elif command == "report_dues":
        if len(rest_arguments) == 1:
            uname = rest_arguments[0]
            print(get_dues(uname))
        else:
            print("Wrong input for report dues")
    elif command == "report_credit_limit":
        if len(rest_arguments) == 0:
            print(users_at_credit_limit())
        else:
            print("Wrong input for report users at credit limit")
    elif command == "report_total_dues":
        if len(rest_arguments) == 0:
            print(total_dues())
        else:
            print("Wrong input for report users at credit limit")
    #print(sys.argv[1:])