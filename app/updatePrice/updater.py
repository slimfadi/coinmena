from datetime import datetime
from apscheduler.schedulers.background import BackgroundScheduler
from updatePrice import alphavantageApi

def start():
    scheduler = BackgroundScheduler()
    scheduler.add_job(alphavantageApi.update_price, 'interval', minutes=60)
    scheduler.start()