
import dao

def do_txn(user_name, mname, amount):
    filter_dict = dict()
    filter_dict["name"] = user_name
    users = dao.list_users(filter_dict)
    mdict = dict()
    mdict["name"] = mname
    merchants = dao.list_merchants(mdict)
    if not merchants:
        return "Failed Txn, No merchant found"
    if users:
        user = users[0]
        credit_limit_left = user["credit_limit"] - user["dues"]
        if amount > credit_limit_left:
            return "Failed Txn, limit reached"
        else:
            dao.update_user(user["id"], user["dues"]+amount)
            dao.add_transaction(user["id"], merchants[0]["id"], amount)
    else:
        return "Failed Txn, No user found"