"""
Test
@author Kishan
@date Feb 21, 2022
"""

import sys
sys.path.insert(0,"..")

from exchange_currency.src.services.FixerAPI import FixerAPI

fixer_api   = FixerAPI()
response    = fixer_api.get_result_amount("USD", "GBP", 100)

print(round(response,2))
