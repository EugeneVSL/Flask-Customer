import sqlite3
from flask import g

class DBConnection:

    DATABASE = 'data/customer.db'

    def get_db(self):

        db = getattr(g, '_database', None)
        
        if db is None:
            db = g._database = sqlite3.connect(self.DATABASE)
            
        return db
    
    def close_connection(self):

        db = getattr(g, '_database', None)
        if db is not None:
            db.close()
