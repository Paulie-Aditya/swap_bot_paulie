import requests
import config_swap_bot
import getcryptocurrencies_script

def refund(user, value, coin):
    value = float(value)
    value = int(value * (10**getcryptocurrencies_script.scaling_dict[coin]))
    print(value)
    tipping_url = 'https://api.tip.cc/api/v0/tips'
    tipping_json = {
        "service": "discord", 
        "recipient": str(user) ,
        "amount": {
                "value": "",
                "currency": ""
            }
    }
    tipping_json["amount"]['value'] = str(value)
    tipping_json["amount"]['currency'] = coin

    x = requests.post(tipping_url, json = tipping_json, headers={'accept':'application/json','Authorization': f'Bearer {config_swap_bot.tipcc_api_key}', 'Content-Type': 'application/json'})
    print(x.text)
    print(x.status_code)
    return x

#refund(464445762986704918,"0.00056","BTC")
