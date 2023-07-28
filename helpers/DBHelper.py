import sqlite3
import sys

class DBHelper:
    def __init__(self, config):
        self.path_to_db = config['sqlite_config']['path']
        self.config = config

    def query_latest_result_id(self):
        try:
            conn = sqlite3.connect(self.path_to_db)
            cursor = conn.cursor()
            res = cursor.execute(f"SELECT {self.config['sqlite_config']['fields'][0]} "
            f"FROM {self.config['sqlite_config']['table_name']} "
            f"ORDER BY {self.config['sqlite_config']['fields'][0]} DESC LIMIT 1").fetchone()
            conn.close()

            return res[0]
        except Exception as e:
            print('An error has occurred while querying records in the SQLite Database')
            print(repr(e))
            sys.exit('QUERY DATABASE')

    def insert_records(self, lst_records):
        import datetime
        from helpers.KinoHelper import KinoHelper
        try:
            print(f'Inserting {len(lst_records)} new records [...]')
            lst_values = []
            insert_statement = f"INSERT INTO {self.config['sqlite_config']['table_name']} ({', '.join(self.config['sqlite_config']['fields'])}) VALUES (?, ?, ?, ?, ?)"
            for record in lst_records:
                date_obj = datetime.datetime.strptime(record['drawingDate'], '%Y-%m-%dT%H:%M:%S')
                lst_values.append((record['electronicDrawingID'], record['drawingNumber'], f"{record['results']}",
                f"{int(datetime.datetime.timestamp(date_obj))}", f"{KinoHelper.sort_record(record['results'])}"))

            # Connect to SQLite DB
            conn = sqlite3.connect(self.path_to_db)
            cursor = conn.cursor()

            # Execute insert statement
            cursor.executemany(insert_statement, lst_values)
            conn.commit()

            # Close the connection
            conn.close()

        except Exception as e:
            print(f'An error has occurred while adding records to the {self.config["sqlite_config"]["table_name"]} table')
            print(repr(e))
            sys.exit('INSERT DATABASE')
