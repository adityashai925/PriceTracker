import requests
from bs4 import BeautifulSoup


class PriceFetcher:
    def __init__(self):
        """
        Obtains the price/prices of items.
        """
        self.ITEMS = [
            {
                "name": "Acer ED270R 27 inch Monitor",
                "url": "https://www.amazon.in/dp/B08K9YLTJ7/ref=cm_sw_em_r_mt_dp_V0B240J9MAMABXRD964K?_encoding=UTF8&psc=1"
            },
            {
                "name": "Ryzen 5 3600",
                "url": "https://www.amazon.in/dp/product/B07STGGQ18/ref=ox_sc_saved_title_9?smid=A14CZOWI0VEHLG&psc=1"
            },
        ]

    def get_price(self, url):
        """
        Returns the price of the item of the given url.
        """
        HEADERS = {
            "authority": "www.amazon.in",
            "method": "GET",
            "path": "/gp/navigation/ajax/generic.html?ajaxTemplate=hMenuDesktopFirstLayer&pageType=Detail&hmDataAjaxHint=1&isFreshRegion=false&isFreshCustomer=false&isPrimeMember=false&isPrimeDay=false&isSmile=false&regionalStores%5B%5D=ctnow&regionalStores%5B%5D=ctnow&isBackup=false&firstName=false&navDeviceType=desktop&hashCustomerAndSessionId=0fa74c948d8ea9daee362ea614845374d2627ce8&isExportMode=false&environmentVFI=AmazonNavigationCards%2Fdevelopment%40B6048321973-AL2_x86_64&languageCode=en_IN",
            "scheme": "https",
            "accept": "text/html, */*; q=0.01",
            "accept-encoding": "gzip, deflate, br",
            "accept-language": "en-US,en;q=0.9",
            "cookie": "session-id=258-1633177-3748818; i18n-prefs=INR; ubid-acbin=260-3159186-1138626; session-token=RCSe/rftGhQJzV8GKJoa1XkpiXcvr4+IdHEcTtjr/BKiA9HWTA+vGHTgeOLqrMTYWMQMRrZ5WKiGimScqyz2YiAK0MyFofJKDWTUqJDTFsBDNnH0bX/6OGadM6kKtDyD4f3c21sFTaXr9WFwbEJjoHfiQmvWCOa3s/5sExoz9FmNKFwEr6XHTJFokxnffOe9k9m+ogvYCaX4u27aVNubGT8h+ph9NDipv5iC4GGm/nZgNUpj/0Xo/iUuMdNkMj5n; session-id-time=2082758401l; visitCount=2; csm-hit=tb:AZM5XQV25D7ZBXYF3K6P+s-KRHT97V0HXDX0441STEW|1622367665538&t:1622367665538&adb:adblk_no",
            "downlink": "10",
            "ect": "4g",
            "referer": "https://www.amazon.in/dp/B08K9YLTJ7/ref=cm_sw_em_r_mt_dp_V0B240J9MAMABXRD964K?_encoding=UTF8&psc=1",
            "rtt": "100",
            "sec-ch-ua": "\" Not A;Brand\";v=\"99\", \"Chromium\";v=\"90\", \"Google Chrome\";v=\"90\"",
            "sec-ch-ua-mobile": "?0",
            "sec-fetch-dest": "empty",
            "sec-fetch-mode": "cors",
            "sec-fetch-site": "same-origin",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36",
            "x-requested-with": "XMLHttpRequest",
        }

        response = requests.get(url, headers=HEADERS)
        content = response.content
        page_soup = BeautifulSoup(content, "html.parser")

        price = int(page_soup.find("span", {"id": "priceblock_ourprice"}).get_text().replace(",", "")[2:-3])
        return price

    def get_prices(self):
        """
        Returns a list of dictionaries of price per item.
        """

        prices = []

        for item in self.ITEMS:
            name = item["name"]
            url = item["url"]
            price = self.get_price(url)

            prices.append(
                {
                    "name": name,
                    "price": price,
                }
            )

        return prices


if __name__ == "__main__":
    Prices = PriceFetcher()
    price_list = Prices.get_prices()
    # print(price_list)

