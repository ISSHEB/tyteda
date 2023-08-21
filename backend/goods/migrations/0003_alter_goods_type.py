# Generated by Django 3.2 on 2023-08-17 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0002_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='type',
            field=models.CharField(blank=True, choices=[('hot_dishes', 'Горячие блюда'), ('soups', 'Супы'), ('paste', 'Паста'), ('snacks', 'Закуски'), ('salads', 'Салаты'), ('side_dishes', 'Гарниры'), ('pizza', 'Пицца'), ('burgers', 'Бургеры'), ('dessert', 'Десерты'), ('drinks', 'Напитки'), ('khachapuri', 'Хачапури'), ('ossetian_pies', 'Осетинские пироги'), ('sauces', 'Соусы'), ('dishes_grill', 'Блюда на мангале'), ('rolls', 'Роллы'), ('beer_snacks', 'Пивные закуски'), ('bread', 'Хлеб'), ('wok', 'Вок'), ('children_menu', 'Детское меню'), ('seasonal_dishes', 'Сезонные блюда')], max_length=50, null=True, verbose_name='Тип блюда'),
        ),
    ]