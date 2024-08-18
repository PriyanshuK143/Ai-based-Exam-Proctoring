import sqlite3
from flask import g

def connect_to_databasetea():
    sql = sqlite3.connect("tealogreg.db")
    sql.row_factory = sqlite3.Row
    return sql



def getDatabasetea():
    if not hasattr(g, "tealogreg"):
        g.logreg = connect_to_databasetea()
    return g.tealogreg