import sqlite3
import os
def init_simple():
    if os.path.exists("simpl.db"):
        os.remove("simpl.db")   
    conn = sqlite3.connect('simpl.db')
    conn.execute('''CREATE TABLE USERS
        (ID INTEGER  PRIMARY KEY AUTOINCREMENT,
        NAME           TEXT    NOT NULL UNIQUE,
        EMAIL_ID       TEXT     NOT NULL,
        CREDIT_LIMIT   REAL,
        DUES         REAL);''')

    conn.execute('''CREATE TABLE MERCHANTS
        (ID INTEGER  PRIMARY KEY     NOT NULL,
        NAME           TEXT    NOT NULL,
        DISCOUNT         REAL);''')

    conn.execute('''CREATE TABLE TXN
        (ID            INTEGER  PRIMARY KEY     NOT NULL,
        USER_ID        INT     NOT NULL,
        MID            INT     NOT NULL,
        AMOUNT         REAL,
        TXN_STATE      INT     NOT NULL);''')
    conn.close()

def add_user(name, email, credit_limit):
    conn = sqlite3.connect('simpl.db')
    conn.execute("INSERT INTO USERS (NAME,EMAIL_ID,CREDIT_LIMIT,DUES) \
      VALUES ('%s', '%s', '%s', 0)" %(name, email, credit_limit))
    conn.commit()
    conn.close()

def list_users(filter=dict()):
    conn = sqlite3.connect('simpl.db')
    query = "SELECT id, NAME, EMAIL_ID, CREDIT_LIMIT, DUES from USERS"
    where_clause = ""
    if filter:
        where_clause = where_clause  + " where "
        if "name" in filter:
            where_clause = where_clause  + "NAME = '%s'" %(filter["name"])
        if "at_credit_limit" in filter and filter["at_credit_limit"]:
            where_clause = where_clause  + "CREDIT_LIMIT = DUES"
        query = query + where_clause

    users = []
    cursor = conn.execute(query)
    for row in cursor:
        user = dict()
        user["id"] = row[0]
        user["name"] = row[1]
        user["email_id"]  = row[2]
        user["credit_limit"] = row[3]
        user["dues"] = row[4]
        users.append(user)
    conn.close()
    return users

def update_user(user_id, target_dues):
    conn = sqlite3.connect('simpl.db')
    conn.execute("UPDATE USERS set DUES = %s where ID = %s"%(target_dues, user_id))
    conn.commit()
    conn.close()

def update_user_with_name(user_name, target_dues):
    conn = sqlite3.connect('simpl.db')
    conn.execute("UPDATE USERS set DUES = %s where NAME = %s"%(target_dues, user_name))
    conn.commit()
    conn.close()

def add_merchant(name, discount):
    conn = sqlite3.connect('simpl.db')
    conn.execute("INSERT INTO MERCHANTS (NAME,DISCOUNT) \
      VALUES ('%s','%s')" %(name, discount))
    conn.commit()
    conn.close()

def update_merchant(mid, discount):
    conn = sqlite3.connect('simpl.db')
    conn.execute("UPDATE MERCHANTS set DISCOUNT = %s where ID = %s"%(discount, mid))
    conn.commit()
    conn.close()

def list_merchants(filter=dict()):
    conn = sqlite3.connect('simpl.db')
    query = "SELECT id, NAME, DISCOUNT from MERCHANTS"
    where_clause = ""
    if filter:
        where_clause = where_clause  + " where "
        if "name" in filter:
            where_clause = where_clause  + "NAME = '%s'" %(filter["name"])
            query = query + where_clause
    merchants = []
    cursor = conn.execute(query)
    for row in cursor:
        user = dict()
        user["id"] = row[0]
        user["name"] = row[1]
        user["discount"]  = row[2]
        merchants.append(user)
    conn.close()
    return merchants

def add_transaction(user_id, m_id, amount):
    conn = sqlite3.connect('simpl.db')
    conn.execute("INSERT INTO TXN (USER_ID,MID, AMOUNT, TXN_STATE) \
      VALUES ('%s','%s', '%s', '%s')" %(user_id, m_id, amount, 1))
    conn.commit()
    conn.close()








