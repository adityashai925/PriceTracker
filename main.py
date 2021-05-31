import json

from PriceFetcher import PriceFetcher
from PriceComparer import PriceComparer
# from EmailSender import EmailSender

PRICE_DATA_FILE_NAME = "price-data.json"

with open(PRICE_DATA_FILE_NAME, "r") as price_read_file:
    ITEMS_DATA = json.load(price_read_file)

Prices = PriceFetcher(ITEMS_DATA)
new_prices_data = Prices.get_prices()

with open(PRICE_DATA_FILE_NAME, "w") as price_write_file:
    json.dump(new_prices_data, price_write_file, indent=4)

Comparer = PriceComparer(ITEMS_DATA, new_prices_data)
changed_prices = Comparer.check_prices()

if len(changed_prices) >= 1:
    for item in changed_prices:
        print(f"Price of {item['name']} has {item['price-diff']}d from {item['old-price']} to {item['new-price']}.")

else:
    print("No Change in prices.")
