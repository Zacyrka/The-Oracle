import sqlite3

def create_database():
    """
    Create a SQLite database and define a table for storing player information if it doesn't exist.

    This function establishes a connection to the database and defines the table structure with columns
    for player information.

    Args:
        None

    Returns:
        None
    """
    connection = sqlite3.connect('zaidejuInfo.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS zaidejai (
            id INTEGER PRIMARY KEY,
            vardas TEXT,
            pavarde TEXT,
            pozicija TEXT,
            marskineliu_numeris INTEGER
        )
    ''')
    connection.close()

def add_player(vardas, pavarde, pozicija, numeris):
    """
        Add a new player to the SQLite database.

        This function inserts a new player's information (name, surname, position, and jersey number) into the database.

        Args:
            vardas (str): The player's first name.
            pavarde (str): The player's last name.
            pozicija (str): The player's position.
            numeris (int): The player's jersey number.

        Returns:
            None
    """
    connection = sqlite3.connect('zaidejuInfo.db')
    cursor = connection.cursor()

    cursor.execute('''
            INSERT INTO zaidejai (vardas, pavarde, pozicija, marskineliu_numeris)
            VALUES (?, ?, ?, ?)
        ''', (vardas, pavarde, pozicija, numeris))

    connection.commit()
    connection.close()

def get_players():
    """
        Retrieve a list of players from the SQLite database.

        This function queries the database to retrieve a list of all players' information.

        Returns:
            list: A list of player records, where each record is a tuple containing the player's information
                (id, vardas, pavarde, pozicija, marskineliu_numeris).
    """
    connection = sqlite3.connect('zaidejuInfo.db')
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM zaidejai")
    players = cursor.fetchall()
    connection.close()
    return players
