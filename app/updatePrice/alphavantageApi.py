import json
import urllib.request as rq
from exchange.models import BtcPrice
from django.conf import settings
from django.utils import timezone


def update_price():
    url = 'https://www.alphavantage.co/query?function=CURRENCY_EXCHANGE_RATE&from_currency=BTC&to_currency=USD&apikey=' + settings.ALPHA_VANTAGE_APIKEY
    html = rq.urlopen(url).read()
    data = json.loads(html.decode('utf-8'))
    latest_price = float(data["Realtime Currency Exchange Rate"]['9. Ask Price'])
    new_value = BtcPrice(price=latest_price, time=timezone.now())
    new_value.save()
    return latest_price