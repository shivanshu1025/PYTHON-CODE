import cx_Oracle
class connection:
    def __init__(self):
        connection.con = cx_Oracle.connect('system/system@localhost/orcl')
        if connection.con!=None:
            print('CONNECTION ESTABLISHED')
            #connection.cur=connection.con.cursor()


