class PriceComparer:
    def __init__(self, old_data, new_data):
        """
        Checks if there is a change in prices.
        """
        self.OLD_DATA = old_data
        self.NEW_DATA = new_data

    def check_prices(self):
        """
        Returns a list of the items which have a change in prices.
        """

        changed_item_prices = []

        if len(self.OLD_DATA) != len(self.NEW_DATA):
            raise Exception("Number of items in both lists is different.")

        for item_num in range(len(self.OLD_DATA)):
            old_name = self.OLD_DATA[item_num]["name"]
            new_name = self.OLD_DATA[item_num]["name"]

            old_price = self.OLD_DATA[item_num]["price"]
            new_price = self.NEW_DATA[item_num]["price"]

            if old_name != new_name:
                raise Exception("Items are not ordered correctly.")

            if old_price != new_price:
                price_diff = new_price - old_price

                if price_diff > 0:
                    increase_decrease = "increase"
                else:
                    increase_decrease = "decrease"

                changed_item_prices.append(
                    {
                        "name": old_name,
                        "old-price": old_price,
                        "new-price": new_price,
                        "price-diff": increase_decrease,
                    }
                )

        return changed_item_prices


if __name__ == "__main__":
    pass