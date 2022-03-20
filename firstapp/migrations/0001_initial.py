# Generated by Django 3.0.8 on 2020-10-11 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IndividualBanks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30, verbose_name='Банк')),
                ('first', models.IntegerField(verbose_name='Максимальная цена обслуживания в год')),
                ('second', models.FloatField(verbose_name='Процент перевода в другие банки')),
                ('third', models.FloatField(verbose_name='Процент перевода внутри банка')),
                ('fourth', models.FloatField(verbose_name='Комиссия на пополнение')),
                ('fifth', models.BooleanField(verbose_name='Online-Банк')),
                ('sixth', models.BooleanField(verbose_name='Мобильное приложение')),
                ('seventh', models.BooleanField(verbose_name='SMS-информирование')),
                ('eighth', models.BooleanField(verbose_name='Telegramm Бот')),
                ('nineth', models.BooleanField(verbose_name='Круглосуточная поддержка')),
                ('tenth', models.BooleanField(verbose_name='Конвертация валюты')),
                ('eleventh', models.BooleanField(verbose_name='Оплата услуг (ЖКХ, Интернет, TV и т.д.)')),
                ('twelveth', models.BooleanField(verbose_name='Оплата кредита')),
                ('thirteenth', models.BooleanField(verbose_name='Открытие вклада')),
                ('fourteenth', models.BooleanField(verbose_name='E-involving')),
                ('fifteenth', models.BooleanField(verbose_name='Private banking')),
            ],
            options={
                'verbose_name': 'Банк для физических лиц',
                'verbose_name_plural': 'Банки для физических лиц',
            },
        ),
    ]
