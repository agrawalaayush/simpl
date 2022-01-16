import dao


def add_users(name, email, credit_limit):
    return dao.add_user(name, email, credit_limit)


def get_dues_of_user(name):
    filter = dict()
    filter["name"] = name
    user = dao.list_users(filter)
    if user:
        return user[0]["dues"]

def get_users_at_credit_limit():
    print("Get Users at credit limit")
    filter = dict()
    filter["at_credit_limit"] = True
    user = dao.list_users(filter)
    return user

def total_dues():
    filter = dict()
    users = dao.list_users(filter)
    dues = 0.0
    for user in users:
        dues = dues + user["dues"]
    return dues

def update_user(user_id, dues):
    dao.update_user(user_id, dues)

def payback_user(user_name, amount):
    filter = dict()
    filter["name"] = user_name
    users = dao.list_users(filter)
    if users:
        user = users[0]
        current_dues =  user["dues"]
        if amount > current_dues:
            return "Failed Txn, Paying more money than dues"
        else:
            dao.update_user(user["id"], user["dues"]-amount)
    else:
        return "Failed txn, No users found"

