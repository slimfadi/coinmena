from django.shortcuts import render
from django.conf import settings
from exchange.models import BtcPrice
from django.http import JsonResponse
from updatePrice import alphavantageApi

from django.http import HttpResponseForbidden

def quote(request):


    latest_row = None

    if request.method == "GET":
        token = request.GET.get("token",None)
    else:
        token = request.POST.get("token",None)

    if token != "123456":
        return HttpResponseForbidden({"no access"},content_type="text/json")

    if request.method == "GET":
        latest_row = BtcPrice.objects.last()


    if latest_row is None :
        latest_price = alphavantageApi.update_price()
        time = "now"
    else:
        latest_price = latest_row.price
        time = latest_row.time
    return JsonResponse({"price":latest_price,"time_updated":time})
