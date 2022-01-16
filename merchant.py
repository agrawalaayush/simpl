import dao


def add_merchant(name, discount):
    dao.add_merchant(name, discount)

def update_merchant(mname, discount):
    filter = dict()
    filter["name"] = mname
    merchants = list_merchants(filter)
    if merchants:
        merchant = merchants[0]
        dao.update_merchant(merchant["id"], discount)
    else:
        return "No merchant found with %s"%(mname)

def list_merchants(filter):
    return dao.list_merchants(filter)

def get_discount(mname):
    filter = dict()
    filter["name"] = mname
    merchants = list_merchants(filter)
    if merchants:
        return merchants[0]["discount"]
    else:
        return "No merchant found with %s"%(mname)