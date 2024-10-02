import pyodbc

"""
This has been validated as working 2024-09-29

"""



try:
    conn = cnxn = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};SERVER=127.0.0.1;DATABASE=PACA;UID=pacauser;PWD=pacauser;TrustServerCertificate=YES;Encrypt=YES', autocommit=True)
    cnxn.setencoding('utf-8') # This connection needs to occur first
    cursor = conn.cursor() # Cursor is necessary for it to function properly
    cursor.execute("{CALL paca.getAccounts_v1}") # This will be moved along with the connection
    #cursor.commit()
    rows = cursor.fetchall()
    data = [(row.ACCOUNT_NUM, row.ACCOUNT_HONORIFICS, row.ACCOUNT_FIRST_NAME,row.ACCOUNT_LAST_NAME, row.ACCOUNT_SUFFIX,row.ACCOUNT_STREET_ADD_1,row.ACCOUNT_STREET_ADD_2,row.ACCOUNT_CITY,row.ACCOUNT_STATE,row.ACCOUNT_ZIP,row.ACCOUNT_PO_BOX,row.ACCOUNT_DATE_START,row.ACCOUNT_DATE_RENEWAL,row.ACCOUNT_TYPE) for row in rows] # rows contains cursor.fetchall()
    print(data)

except Exception as ERROR:
            print(ERROR)
finally:
    cursor.close()
    conn.close()
    #PythonListener.disconnect_connection(conn) # We need to disconnect at some point when the application closes.



"""  i = 0
            while i < tempcount:
                logging.debug(f"Current i Value {i}")
                table.data.append(i,[data[i]])
                i += 1
            
        TIMEOUT = 20  # Max number of seconds to wait for procedure to finish execution
        slept = 0
        while cursor.nextset():
            if slept >= TIMEOUT:
                break
            time.sleep(1)
            slept += 1"""