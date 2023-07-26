import datetime
import os
import sys

from helpers.DBHelper import DBHelper
from helpers.FileHelper import FileHelper
from helpers.KinoHelper import KinoHelper

def main():
    print(f'Scrip start: {datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")}\n')
    cwd = os.path.dirname(__file__)

    config = FileHelper.load_yaml(os.path.join(cwd, 'config.yaml'))
    if not config:
        sys.exit('Unable to load config file')

    # Create a KinoHelper instance
    game_helper_instance = KinoHelper(config)
    # Create a DBHelper instance
    sqlite_helper_instance = DBHelper(config)

    # Query latest results and filter records to be added to the database.
    results = game_helper_instance.query_kino_results(sqlite_helper_instance)

    if len(results) > 0:
        # Store the queried values in sqlite3 database
        sqlite_helper_instance.insert_records(results)
    else:
        print('No results to insert into the SQLite Database')

    print(f'\nScrip finished: {datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")}')

if __name__ == "__main__":
    main()