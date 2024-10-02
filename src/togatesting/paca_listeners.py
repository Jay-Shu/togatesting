import toga
import pyodbc


class PythonListener(toga.sources.Listener):
    def __init__(self):
        global t, cnxn
        self.listener = toga.sources.Listener
        t = self.listener
        cnxn = self.init_connection()

    def init_connection():
       global cnxn
       cnxn = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};SERVER=127.0.0.1;DATABASE=PACA;UID=pacauser;PWD=pacauser;TrustServerCertificate=YES;Encrypt=YES', autocommit=True)
       cnxn.setencoding('utf-8')
       pyodbc.pooling=True
            #params = None
       pyodbc.dataSources()
       return cnxn
    
    def disconnect_connection(conn):
        global dccc
        dccc = conn.close()
        try:
            dccc
        except Exception as ERROR:
            print(ERROR)
        finally:
            print("Successful Connection Close.")
        return


class PythonSources(toga.sources.Source):
    def _create_listeners(self):
        global psource
        self.source = toga.sources.Source

        cnxn = PythonListener.init_connection()

        toga.sources.Source.add_listener(cnxn)

        pass
    pass

def main():
    return PythonListener(),PythonSources()