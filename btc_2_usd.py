import requests

def usd_to_btc(usd_val):
    btc_price_url = "https://blockchain.info/tobtc?currency=USD&value=" + str(usd_val)
    response = requests.get(btc_price_url)
    return str(response.text)


def btc_to_usd(btc_val):
    usd_price_url = "https://blockchain.info/ticker"
    response = requests.get(usd_price_url)
    total_val = float(response.json()["USD"]["last"]) * float(btc_val)
    return str('{0:,.2f}'.format(total_val))


def main():
    converting = True
    print("Welcome to BTC converter!\nPlease select an option")
    while converting:
        print("")
        print("1. Convert USD to BTC")
        print("2. Convert BTC to USD")
        print("3. Exit app")

        option = input("Option: ")
        if option == "1":
            print("Enter USD value:")
            usd_val = input()
            print("Total BTC: " + usd_to_btc(usd_val))

        elif option == "2":
            print("Enter BTC value:")
            btc_val = input()
            print("Total USD: " + btc_to_usd(btc_val))

        elif option == "3":
            converting = False

        else:
            print("Not a valid option!\nPlease select a valid option")

if __name__ == "__main__":
    main()