import sqlite3
import time
Time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
con = sqlite3.connect("pop.db")


def addProduct(params):
    cur = con.cursor()
    sql = 'INSERT INTO "product" ( "Name", "price", "discount", "costprice", "count", "sold", "create_date", "production_date", "expiration_date" )VALUES( ?, ?, ?, ?,?,?,?,?,? )'
    cur.execute(sql, params)
    con.commit()


params = ("辣条", 1.5, 1, 0.5, 1000, 0, "2020/8/5 13: 00",
          "2020/8/2 12: 00",
          "2021/8/8 16: 00")
addProduct(params)


def addCar(params, params1):
    cur = con.cursor()
    sql = 'INSERT INTO "car" ( "count", "create_date", "price", productid ) VALUES ( ?,?, ?,? )'
    cur.execute(sql, params)
    cur = con.cursor()
    cur.execute('UPDATE product set count=count-? WHERE id=?', params1)
    con.commit()


params = (1, "2020-08-05 13: 00", 1.5, 1)
params1 = (1, 1)
addCar(params, params1)


def addorder(params):
    cur = con.cursor()
    cur.execute(
        'INSERT INTO "order" ("total", "create_Time") VALUES (?,?)', params)
    con.commit()
    return cur.lastrowid


params = (0, "2020-08-08 13: 00")

id = addorder(params)


def jiesuan1(params, params1):
    cur = con.cursor()
    cur.execute('SELECT * FROM "car" WHERE order_id is NULL')
    cur.execute('update car set order_id = ? WHERE id=?', params)
    cur.execute('UPDATE "order" set total= total + ? WHERE id=?', params1)


params = (id, 1)
params1 = (1*1.5, 1)
jiesuan1(params, params1)


def zhifu(parma1, params2):
    cur = con.cursor()

    cur.execute(
        'UPDATE "order" SET "pay_Time" = CURRENT_TIMESTAMP WHERE id = ?', params1)
    cur.execute('UPDATE "product" SET sold= sold + ? WHERE id=?', params2)


param1 = (id,)
params2 = (1, 1)
zhifu(param1, params2)
con.commit()

