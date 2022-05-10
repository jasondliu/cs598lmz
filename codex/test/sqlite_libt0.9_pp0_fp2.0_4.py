import ctypes
import ctypes.util
import threading
import sqlite3
import os
import stat


class InsertValuesWorker(threading.Thread):
    def __init__(self, output_queue, chunk, table_name, conn, num_columns_in_table):
        threading.Thread.__init__(self)
        self.output_queue = output_queue
        self.chunk = chunk
        self.table_name = table_name
        self.conn = conn
        self.num_columns_in_table = num_columns_in_table

    def run(self):
        values = []
        for row in self.chunk:
            row = [str(item) for item in row]
            values.append("(" + ",".join(row) + ")")

        if values:
            query = "INSERT OR IGNORE INTO %s VALUES %s" % (
                self.table_name, ",".join(values))
            self.conn.execute(query)

        self.output_queue.put(values)

