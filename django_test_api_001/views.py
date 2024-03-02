from urllib import request

from django.http import Http404
from django.shortcuts import render

# Create your views here.

from rest_framework import views, generics, status, permissions
from rest_framework.decorators import permission_classes, api_view
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from rest_framework.status import HTTP_200_OK, HTTP_204_NO_CONTENT
from rest_framework.views import APIView

from .models import Employee, Client, Product, Order, Statistic
from rest_framework.response import Response
from .serializers import FirstViewSerializer, SecondViewSerializer, ThirdViewSerializer

from django.views.generic.dates import YearArchiveView




class ViewDetail_One(generics.RetrieveAPIView):
    queryset = Statistic.objects.all()
    serializer_class = FirstViewSerializer
    permission_classes = [IsAdminUser]

    def detail(self, request, pk, year, month):
        day = 1
        if request.method == 'GET':
            statistic = Statistic.objects.get(pk=pk, created_date=year - month - day)
            serializer = FirstViewSerializer(statistic)
            return Response(serializer.data)
        pass


class ViewDetail_Two(generics.ListAPIView):
    queryset = Statistic.objects.all()
    serializer_class = SecondViewSerializer
    permission_classes = [IsAdminUser]

    def detail(self, request, pk, year, month):
        day = 1
        if request.method == 'GET':
            serializer = FirstViewSerializer(statistic)
            return Response(serializer.data)
        pass
        

class ViewDetail_Three(generics.RetrieveAPIView):
    queryset = Statistic.objects.all()
    serializer_class = SecondViewSerializer
    permission_classes = [IsAdminUser]

    def detail(self, request, pk, year, month):
        day = 1
        if request.method == 'GET':
            statistic = Statistic.objects.get(pk=pk, created_date=year - month - day)
            serializer = ThirdViewSerializer(statistic)
            return Response(serializer.data)
        pass


