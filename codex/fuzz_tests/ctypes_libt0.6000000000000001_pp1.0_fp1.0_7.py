import ctypes
ctypes.windll.user32.MessageBoxW(0, "Your text", "Your title", 1)

# def get_dao_recordset(db, sql):
#     """ Get a recordset from a DAO connection.
#     db: DAO database object.
#     sql: SQL string.
#     """
#     recset = db.OpenRecordset(sql, dbOpenDynaset)
#     return recset

# def get_dao_db(mdb_file):
#     """ Get a DAO database connection.
#     mdb_file: Path to Microsoft Access MDB file.
#     """
#     # Access 2003.
#     # acc = win32com.client.Dispatch(r"DAO.DBEngine.36")
#     # db = acc.OpenDatabase(mdb_file)
#     # Access 2007.
#     acc = win32com.client.Dispatch(r"DAO.DBEngine.120")
#     db = acc.OpenDatabase(mdb_file)
#     return db


# def get_dao_record
