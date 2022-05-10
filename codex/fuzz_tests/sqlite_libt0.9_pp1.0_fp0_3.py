import ctypes
import ctypes.util
import threading
import sqlite3

class radio_error(Exception): pass
class database_error(Exception): pass

class radio_run( threading.Thread ):
    """
    Class representing a thread to implement a polling loop
    """
    def __init__(self, db_file ):
        """
        Constructor. Stores database connection in `db`
        """
        self.db = sqlite3.connect( db_file )
        threading.Thread.__init__(self)
    
    def run(self):
        """
        Set up a polling loop.
        """
        sql = self.db.cursor()  # for polling
        sql.execute("SELECT NOW()")
        # Start polling
        while True:
            result = sql.fetchone()
            # this will make it slow down the main thread's polling function
            # but I'm not sure of any better way to do it.
            time.sleep( 2 )

    def quit(self):
        """
        Attempt to end the polling loop and close the database connection.
        """
        self.db.close()

class radio(
