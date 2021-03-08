from django.apps import AppConfig


class ExchangeConfig(AppConfig):
    name = 'exchange'

    def ready(self):
        from updatePrice import updater
        updater.start()
