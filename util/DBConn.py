import pyodbc
from util.DBPropertyUtil import PropertyUtil


class DBConnection:
    def __init__(self):
        conn_str = PropertyUtil.get_property_String()
        self.conn = pyodbc.connect(conn_str)
        self.cursor = self.conn.cursor()

    def close(self):
        self.cursor.close()
        self.conn.close()
