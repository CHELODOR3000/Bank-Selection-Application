from django.db import models


class IndividualBanks(models.Model):
    name = models.CharField("Банк", max_length=30)
    first = models.IntegerField("Максимальная цена обслуживания в год")
    second = models.FloatField("Процент перевода в другие банки")
    third = models.FloatField("Процент перевода внутри банка")
    fourth = models.FloatField("Комиссия на пополнение")

    fifth = models.BooleanField("Online-Банк")
    sixth = models.BooleanField("Мобильное приложение")
    seventh = models.BooleanField("SMS-информирование")
    eighth = models.BooleanField("Telegramm Бот")
    nineth = models.BooleanField("Круглосуточная поддержка")
    tenth = models.BooleanField("Конвертация валюты")
    eleventh = models.BooleanField("Оплата услуг (ЖКХ, Интернет, TV и т.д.)")
    twelveth = models.BooleanField("Оплата кредита")
    thirteenth = models.BooleanField("Открытие вклада")
    fourteenth = models.BooleanField("E-involving")
    fifteenth = models.BooleanField("Private banking")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Банк для физических лиц"
        verbose_name_plural = "Банки для физических лиц"


class LegalBanks(models.Model):
    name = models.CharField("Банк", max_length=30)
    first = models.IntegerField("Стоимость внедрения")
    second = models.IntegerField("Стоимость обслуживания (руб./мес.)")
    third = models.FloatField("Комиссия на перевод (%)")

    fourth = models.BooleanField("Online-bank")
    fifth = models.BooleanField("Мобильное приложение")
    sixth = models.BooleanField("SMS-информирование")
    seventh = models.BooleanField("Ведение переписки с банком")
    eighth = models.BooleanField("Круглосуточная поддержка")
    nineth = models.BooleanField("Конвертация валюты")
    tenth = models.BooleanField("Интеграция с 1С")
    eleventh = models.BooleanField("Получение информации о расчетном счете")
    twelveth = models.BooleanField("Платежи и переводы валютой")
    thirteenth = models.BooleanField("Продажа валюты")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Банк для юридических лиц"
        verbose_name_plural = "Банки для юридических лиц"