import toga
from toga.style import Pack
from toga.style.pack import COLUMN, ROW
import pyodbc


# Database connection function (persistent connection)
def connect_to_database():
    conn_str = (
        "DRIVER={SQL Server};"
        "SERVER=your_server_name;"
        "DATABASE=your_database_name;"
        "UID=your_username;"
        "PWD=your_password;"
    )
    try:
        connection = pyodbc.connect(conn_str)
        print("Database connection established.")
        return connection
    except Exception as e:
        print(f"Error connecting to database: {e}")
        return None


# Function to fetch data from MS SQL database
def fetch_data(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT TOP 10 * FROM your_table")  # Modify your query here
    rows = cursor.fetchall()
    return rows


# Function to open a second window and display results
def open_second_window(widget):
    # Fetch data from the database
    data = fetch_data(connection)

    # Create the second window
    second_window = toga.Window(title="Database Results")

    # Create a label for each row fetched
    labels = []
    for row in data:
        # Join row values into a string
        row_str = ', '.join(str(item) for item in row)
        labels.append(toga.Label(row_str, style=Pack(padding=5)))

    # Add the labels to a box
    second_box = toga.Box(children=labels, style=Pack(direction=COLUMN, padding=10))

    # Add the box to the second window
    second_window.content = second_box

    # Show the second window
    app.windows.add(second_window)
    second_window.show()


# Main application build function
def build(app):
    global connection
    # Initialize persistent database connection
    connection = connect_to_database()

    # Create the main window with a button
    main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

    button = toga.Button("Fetch and Open Results Window", on_press=open_second_window, style=Pack(padding=10))
    main_box.add(button)

    return main_box


# Main app function
def main():
    return toga.App('Main Window with DB Connection', 'org.example.dbwindow', startup=build)


if __name__ == '__main__':
    app = main()
    app.main_loop()
