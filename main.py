import datetime
import os

from helpers.FileHelper import FileHelper
from helpers.KinoHelper import KinoHelper

def main():
    print(f'Scrip start: {datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")}\n')
    cwd = os.path.dirname(__file__)

    config = FileHelper.load_yaml(os.path.join(cwd, 'config.yaml'))

    #Create a KinoHelper instance
    game_helper_instance = KinoHelper(config)

    # Query latest results and filter records to be added to the database.

    # Store the queried values in sqlite3 database

    print(f'\nScrip finished: {datetime.datetime.now().strftime("%Y-%m-%d %I:%M:%S %p")}')

if __name__ == "__main__":
    main()