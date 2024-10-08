"""
Intended for testing various features with Toga.
"""
import tracemalloc
import toga
import time
import logging
logger = logging.getLogger(__name__)

import toga.sources
from toga.style import Pack
from toga.style.pack import COLUMN, ROW, CENTER
from toga.sources import ListSource

from togatesting.poc import *
from togatesting.paca_listeners import *
from togatesting.function_library.accounts import *

tracemalloc.start()

class TogaTesting(toga.App):
    def startup(self):
        logging.basicConfig(
            filename='E:\\scripts\\python\\togatesting\\togatesting.log',
            level=logging.DEBUG,
            format='%(filename)s %(lineno)d %(asctime)s %(message)s %(module)s %(msecs)d'
            )
        self.app = toga.App
        #logging.INFO(self.app)
        """Construct and show the Toga application.
       
        https://docs.python.org/3.12/library/logging.html#logrecord-attributes

        Usually, you would add your application to a main content box.
        We then create a main window (with a name matching the app), and
        show the main window.
        """
        #PythonSources._create_listeners(self)
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
        AccountsClass.accounts_secondary_box(self,widget)
        

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


def main():
    return TogaTesting()

snapshot = tracemalloc.take_snapshot()
top_stats = snapshot.statistics('lineno')

print("[ Top 10 ]")
for stat in top_stats[:10]:
    print(stat)