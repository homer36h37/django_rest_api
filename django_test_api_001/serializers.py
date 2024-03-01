from rest_framework import serializers

from .models import Employee, Client, Product, Order, Statistic


        


class FirstViewSerializer(serializers.ModelSerializer):
    """ Serializer """

    class Meta:
        model = Statistic
        fields = ('full_name_employee', 'quantity_clients', 'quantity_products', 'total_price')



class SecondViewSerializer(serializers.ModelSerializer):
    """ Serializer """

    class Meta:
        model = Statistic
        fields = ('employee', 'full_name_employee', 'quantity_clients', 'quantity_products', 'total_price', 'created_date')


class ThirdViewSerializer(serializers.ModelSerializer):
    """ Serializer """

    class Meta:
        model = Statistic
        fields = ('client', 'full_name_client', 'quantity_clients', 'quantity_products', 'total_price', 'created_date')

