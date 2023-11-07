import sqlite3 as sql


class SQLConnector:
    def __init__(self):
        self.con = sql.connect("./identifier.sqlite")
        self.con.commit()

    def execute_sql(self, sql):
        curs = self.con.cursor()
        curs_res = self.con.cursor().execute(sql)
        curs.close()
        return curs_res

    def get_values_from_table(self, identifier, table):
        return self.execute_sql(f"SELECT {identifier} FROM {table}")

    def insert_values(self, table, values):
        return self.execute_sql(f"INSERT INTO {table} ({values})")

    def modify_values(self, table, column, values):
        return self.execute_sql(f"UPDATE {table} SET {column} = {values}")

    def close_connection(self):
        self.con.commit()
        self.con.close()

if __name__ == '__main__':

    sqlcon = SQLConnector()

    sqlcon.modify_values("xp_values", "xp", 100)

    res = sqlcon.get_values_from_table("xp", "xp_values")

    for row in res:
        print(row[0])

    sqlcon.close_connection()
