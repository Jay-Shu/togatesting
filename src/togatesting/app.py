"""
Intended for testing various features with Toga.
"""
import tracemalloc
import toga

import toga.sources
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER
from toga.sources import TreeSource

from togatesting.poc import *
from togatesting.paca_listeners import *

tracemalloc.start()

class TogaTesting(toga.App):
    def startup(self):
        self.app = toga.App
        """Construct and show the Toga application.

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        main_box = toga.Box(style=Pack(direction=COLUMN))
        
        #accountsLabel = toga.Label('Main Section')
        #main_box.add(accountsLabel)

        accountsButton = toga.Button('Accounts',style=Pack(padding=5),on_press=self._accounts_callback)
        vehiclesButton = toga.Button('Vehicles',style=Pack(padding=5),on_press=self._vehicles_callback)
        homesButton = toga.Button('Homes',style=Pack(padding=5),on_press=self._homes_callback)
        policiesButton = toga.Button('Policies',style=Pack(padding=5),on_press=self._policies_callback)
        vehicleCoveragesButton = toga.Button('Vehicle Coverages',style=Pack(padding=5),on_press=self._vehicle_coverages_callback)
        vehicleClaimsButton = toga.Button('Vehicle Claims',style=Pack(padding=5),on_press=self._vehicle_claims_callback)

        main_box.add(accountsButton)
        main_box.add(vehiclesButton)
        main_box.add(homesButton)
        main_box.add(policiesButton)
        main_box.add(vehicleCoveragesButton)
        main_box.add(vehicleClaimsButton)

        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def _accounts_callback(self,widget):
    # Create the second window
        second_window = toga.Window(title="Accounts")
        #second_label = toga.Label("This is the second window", style=Pack(padding=10))
        second_box = toga.Box(children=[], style=Pack(direction=COLUMN,alignment=CENTER,font_size=14))
        columns = ['ACCOUNT_NUM', 'ACCOUNT_HONORIFICS', 'ACCOUNT_FIRST_NAME', 'ACCOUNT_LAST_NAME', 'ACCOUNT_SUFFIX', 'ACCOUNT_STREET_ADD_1',
                   'ACCOUNT_STREET_ADD_2', 'ACCOUNT_CITY', 'ACCOUNT_STATE', 'ACCOUNT_ZIP', 'ACCOUNT_PO_BOX', 'ACCOUNT_DATE_START', 'ACCOUNT_DATE_RENEWAL', 'ACCOUNT_TYPE']
        
        # Call the method to fetch data from the stored procedure
        data = getAccounts()
        label = toga.Label('Accounts Results',style=Pack(padding=10,font_size=14))
        second_box.add(label)
        
        if data:
        # Populate the table with data
            table = toga.Table(headings=columns, style=Pack(flex=1,font_size=14))
            second_box.add(table)
        
        else:
            error_label = toga.Label('No data found or an error occurred.',style=Pack(padding=10,font_size=14))
            second_box.add(error_label)

        self.content = second_box
        
    
    # Add the second box (content) to the second window
        #second_window.content = second_box
        #second_window.content = GetAccounts()
    # Show the second window
        self.windows.add(second_window)
        second_window.show()

    def _homes_callback(self,widget):
    # Create the second window
        second_window = toga.Window(title="Homes")
        second_label = toga.Label("This is the second window", style=Pack(padding=10))
        second_box = toga.Box(children=[second_label], style=Pack(direction=COLUMN))
    
    # Add the second box (content) to the second window
        second_window.content = second_box
    
    # Show the second window
        self.windows.add(second_window)
        second_window.show()


    def _vehicles_callback(self,widget):
    # Create the second window
        second_window = toga.Window(title="Vehicles")
        second_label = toga.Label("This is the second window", style=Pack(padding=10))
        second_box = toga.Box(children=[second_label], style=Pack(direction=COLUMN))
    
    # Add the second box (content) to the second window
        second_window.content = second_box
    
    # Show the second window
        self.windows.add(second_window)
        second_window.show()


    def _policies_callback(self,widget):
    # Create the second window
        second_window = toga.Window(title="Policies")
        second_label = toga.Label("This is the second window", style=Pack(padding=10))
        second_box = toga.Box(children=[second_label], style=Pack(direction=COLUMN))
    
    # Add the second box (content) to the second window
        second_window.content = second_box
    
    # Show the second window
        self.windows.add(second_window)
        second_window.show()


    def _vehicle_coverages_callback(self,widget):
    # Create the second window
        second_window = toga.Window(title="Vehicle Coverages")
        second_label = toga.Label("This is the second window", style=Pack(padding=10))
        second_box = toga.Box(children=[second_label], style=Pack(direction=COLUMN))
    
    # Add the second box (content) to the second window
        second_window.content = second_box
    
    # Show the second window
        self.windows.add(second_window)
        second_window.show()


    def _vehicle_claims_callback(self,widget):
    # Create the second window
        second_window = toga.Window(title="Vehicle Claims")
        second_label = toga.Label("This is the second window", style=Pack(padding=10))
        second_box = toga.Box(children=[second_label], style=Pack(direction=COLUMN))
    
    # Add the second box (content) to the second window
        second_window.content = second_box
    
    # Show the second window
        self.windows.add(second_window)
        second_window.show()

""" def init_connection():
        cnxn = pyodbc.connect(
                'DRIVER={ODBC Driver 17 for SQL Server};SERVER=127.0.0.1;DATABASE=PACA;UID=pacauser;PWD=pacauser;TrustServerCertificate=YES;Encrypt=YES', autocommit=True)
        cnxn.setencoding('utf-8')
            #params = None
        return cnxn """

def getAccounts():
        try:
            conn = PythonListener.init_connection()
            cursor = conn.cursor()
            cursor.execute("{CALL paca.getAccounts_v1}")
            #cursor.commit()
            #rows = cursor.fetchall()
            data = [(row.ACCOUNT_NUM, row.ACCOUNT_HONORIFICS, row.ACCOUNT_FIRST_NAME,row.ACCOUNT_LAST_NAME, row.ACCOUNT_SUFFIX,row.ACCOUNT_STREET_ADD_1,row.ACCOUNT_STREET_ADD_2,row.ACCOUNT_CITY,row.ACCOUNT_STATE,row.ACCOUNT_ZIP,row.ACCOUNT_PO_BOX,row.ACCOUNT_DATE_START,row.ACCOUNT_DATE_RENEWAL,row.ACCOUNT_TYPE) for row in cursor.fetchall()]
            return data

        except Exception as ERROR:
            print(ERROR)
        finally:
            cursor.close()
            #conn.close()
            #PythonListener.disconnect_connection(conn)
        return data


def main():
    return TogaTesting()

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

print("[ Top 10 ]")
for stat in top_stats[:10]:
    print(stat)