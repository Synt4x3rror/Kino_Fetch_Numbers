import datetime

import requests
import sys
import json

class KinoHelper:
    def __init__(self, config):
        self.config = config

    def __query_latest_records(self, query_results_qty):
        try:
            print('Querying results [...]')
            res = requests.get(f"{self.config['kino_service']['url']}/{self.config['kino_service']['number_game']}/{query_results_qty}")
            if(res.status_code and res.status_code == 200 and res.text):
                return json.loads(res.text)
            else:
                raise Exception('Query resource exception')
        except Exception as e:
            print('An error has occurred while attempting to fetch results form the Loteria Electronica Results API')
            print(repr(e))
            sys.exit('FETCH')

    def query_kino_results(self, sqlite_helper_instance):
        # Determine how many records should be queried from the results API
        results_to_query = self.__get_result_qty_fetch(sqlite_helper_instance)
        if(results_to_query <= 0):
            sys.exit('Not enough time has passed between script runs')

        # Query the latest records in the Loteria Electronica de Puerto Rico
        res = self.__query_latest_records(results_to_query)

        # Check last result on the sqlite database
        last_id = sqlite_helper_instance.query_latest_result_id()

        # Remove the results from results obtained, if necessary
        res = [x for x in res if x['electronicDrawingID'] > last_id]

        return res

    def __get_result_qty_fetch(self, sqlite_helper_instance):
        # Query the sqlite database to obtain last date of most recent result
        last_date = sqlite_helper_instance.query_latest_result_date()
        now = int(datetime.datetime.now().timestamp())
        seconds_per_drawing = self.config['kino_service']['minutes_per_drawing'] * 60
        return int((now-last_date)/seconds_per_drawing)

    @staticmethod
    def sort_record(record_string):
        lst_records = record_string.split('-')
        lst_records.sort()

        return '-'.join(lst_records)
