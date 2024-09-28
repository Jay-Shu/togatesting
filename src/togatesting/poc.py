import pyodbc

class GetAccounts():
    def connection(self):
        try:
            cnxn = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};SERVER=127.0.0.1;DATABASE=PACA;UID=pacauser;PWD=pacauser;TrustServerCertificate=YES;Encrypt=YES', autocommit=False)
            cnxn.setencoding('utf-8')
            params = None
            cursor = cnxn.cursor()
            cursor.execute("{CALL paca.getAccounts_v1}", params)
            #rows = cursor.fetchall()
            data = [(row.ACCOUNT_NUM, row.ACCOUNT_HONORIFICS, row.ACCOUNT_FIRST_NAME,row.ACCOUNT_LAST_NAME, row.ACCOUNT_SUFFIX,row.ACCOUNT_STREET_ADD_1,row.ACCOUNT_STREET_ADD_2,row.ACCOUNT_CITY,row.ACCOUNT_STATE,row.ACCOUNT_ZIP,row.ACCOUNT_PO_BOX,row.ACCOUNT_DATE_START,row.ACCOUNT_DATE_RENEWAL,row.ACCOUNT_TYPE) for row in cursor.fetchall()]
            return data

        except Exception as ERROR:
            print(ERROR)
        finally:
            cursor.close()
            cnxn.close()
        return self