import requests
import sys
import json

class KinoHelper:
    def __init__(self, config):
        self.config = config

    def query_latest_records(self):
        try:
            res = requests.get(f"{self.config['kino_service']['url']}/{self.config['kino_service']['number_game']}/{self.config['kino_service']['drawings_per_request']}")
            if(res.status_code and res.status_code == 200 and res.text):
                return json.loads(res.text)
            else:
                raise Exception('Query resource exception')
        except Exception as e:
            print('An error has occurred while attempting to fetch results form the Loteria Electronica Results API')
            print(repr(e))
            sys.exit('FETCH')