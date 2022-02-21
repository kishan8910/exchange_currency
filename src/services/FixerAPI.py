"""
Class to define all functionalities related to API
@author Kishan
@date Feb 21, 2022
"""
import requests
import json
import os
from requests.adapters import HTTPAdapter
from requests.packages.urllib3.util.retry import Retry

class FixerAPI:

    # constructor
    def __init__(self):
        self.api_access_key = os.getenv('ACCESS_KEY')
        self.api_url        = "http://data.fixer.io/api/latest" 


    # method to receive request and call API url
    # @param from currency, to currency, amount
    # @response buyable amount
    def get_result_amount(self, from_currency, to_currency, amount):
        try:
            response            = self.__call_api('GET')
            response_dict       = json.loads(response.text)

            to_value            = response_dict['rates'][to_currency]
            from_value          = response_dict['rates'][from_currency]
            amount              = amount

            buyable_amount      = (to_value/from_value) * amount 
            return buyable_amount

        except requests.exceptions.RequestException as e:
            print(e.response.text)


    # method to call API url
    # @param HTTP method type
    # @response response
    def __call_api(self, type):
        url             = self.api_url + "?access_key=" + self.api_access_key + "&format=1"
        
        try:
            if type == "GET":
                retry_strategy = Retry(total=1000, 
                                status_forcelist=[106, 404, 403, 500, 501, 502, 503, 504, 505],
                                method_whitelist=["HEAD", "GET", "OPTIONS"])

                adapter = HTTPAdapter(max_retries=retry_strategy)
                http = requests.Session()
                http.mount("https://", adapter)
                http.mount("http://", adapter)
                
                response = http.get(url)
            else:
                response    = "Invalid Request Type"
            return response
        
        except requests.exceptions.RequestException as e:
            raise SystemExit(e)

