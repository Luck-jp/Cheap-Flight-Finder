import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

SHEETY_PRICES_ENDPOINT = os.environ["SHEETY_ENDPOINT"]

class DataManager:

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT)
        data = response.json()
        self.destination_data = data["sheet1"]
        return self.destination_data

    # ==================== Updated the price in the spreadsheet ====================

    def update_lowest_price(self, row_id, new_price):
        new_data = {
            "sheet1": {
                "lowestPrice": new_price
            }
        }
        requests.put(
            url=f"{SHEETY_PRICES_ENDPOINT}/{row_id}",
            json=new_data,
            )
