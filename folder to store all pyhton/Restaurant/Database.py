import sqlite3
class database: 
    def _init_(self, db):
        self.conn = sqlite3.connect(db)
        self.cur = self.conn.cursor()
        self.cur.excecute("CREATE TABLE IF NOT EXISTS shop(id INTEGER PRIMARY KEY, burger")
        self.conn.commit()

    def insert(self, burger, sandwich, pizza):
        self.cur.execute("INSERT")