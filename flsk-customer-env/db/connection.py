import sqlite3
from flask import g


class DBConnection:

    def __init__(self, app):
        self.DATABASE = app.config.get("DATABASE")

    def get_db(self):

        """ Opens the connection to SQLite database.

        Returns:
            connection: A valid SQLite connection. 
        """        
        
        db = getattr(g, '_database', None)
        
        if db is None:
            db = g._database = sqlite3.connect(self.DATABASE)
            
        return db

    def close_connection(self, conn):

        """ Closes the Db connection.
        """     
        if conn is not None:
            conn.close()
