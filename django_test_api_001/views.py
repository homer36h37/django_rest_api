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

# class ViewDetail_One(APIView):
#     permission_classes = [IsAdminUser]
#
#     def get(self, request, pk, year):
#         statistic = Statistic.objects.get(id=pk, year=Statistic.created_date.year, draft=False)
#         serializer = FirstViewSerializer(statistic)
#         return Response(serializer.data)
#
# class ViewDetail_Two(APIView):
#     permission_classes = [IsAdminUser]
#
#     def get(self, request, pk, year):
#         statistic = Statistic.objects.get(id=pk, year=Statistic.created_date.year, draft=False)
#         serializer = SecondViewSerializer(statistic)
#         return Response(serializer.data)
#
# class ViewDetail_Three(APIView):
#     permission_classes = [IsAdminUser]
#
#     def get(self, request, pk, year):
#         statistic = Statistic.objects.get(id=pk, year=Statistic.created_date.year, draft=False)
#         serializer = ThirdViewSerializer(statistic)
#         return Response(serializer.data)

# class ViewDetail_One(APIView):
#     permission_classes = [IsAdminUser]
#
#     def get(self, request, pk):
#         statistic = Statistic.objects.get(id=pk, draft=False)
#         serializer = FirstViewSerializer(statistic)
#         return Response(serializer.data)


# class ViewDetail_One(YearArchiveView):
#     queryset = Statistic.objects.all()
#     date_field = "created_date"
#     make_object_list = True
#     allow_future = True
#     serializer_class = FirstViewSerializer
#     permission_classes = [IsAdminUser]





class ViewDetail_One(generics.RetrieveAPIView):
    queryset = Statistic.objects.all()
    serializer_class = FirstViewSerializer
    permission_classes = [IsAdminUser]

    def detail(self, request, pk, year, month):
        day = 1
        # Note the use of `get_queryset()` instead of `self.queryset`
        # Payload.objects.filter(user=user_id, timestamp__range=[start_date, end_date]
        if request.method == 'GET':
            statistic = Statistic.objects.get(pk=pk, created_date=year - month - day)
            # statistic = Statistic.objects.get(pk=pk)
            serializer = FirstViewSerializer(statistic)
            return Response(serializer.data)
        pass






# class ViewDetail_One(generics.ListCreateAPIView):
#     queryset = Statistic.objects.all()
#     serializer_class = FirstViewSerializer
#     permission_classes = [IsAdminUser]
#
#     def detail(self, request, pk, year, month):
#         day = 1
#         # Note the use of `get_queryset()` instead of `self.queryset`
#         # Payload.objects.filter(user=user_id, timestamp__range=[start_date, end_date]
#         statistic = Statistic.objects.filter(pk=pk, created_date=year - month - day)
#         serializer = FirstViewSerializer(statistic)
#         return Response(serializer.data)



    # def list(self, request):
    #     # Note the use of `get_queryset()` instead of `self.queryset`
    #     queryset = self.get_queryset()
    #     serializer = FirstViewSerializer(queryset, many=True)
    #     return Response(serializer.data)









    # def get_object(self, month):
    #     try:
    #         return Statistic.objects.filter(created_date=month)
    #     except Statistic.DoesNotExist:
    #         raise Http404
    #
    # def get_object(self, year):
    #     try:
    #         return Statistic.objects.filter(created_date=year)
    #     except Statistic.DoesNotExist:
    #         raise Http404

# @api_view(['GET'])
# def high_score(request, pk):
#     instance = HighScore.objects.get(pk=pk)
#     serializer = HighScoreSerializer(instance)
#     return Response(serializer.data)

# @api_view(['GET', 'POST'])
# def hello_world(request):
#     if request.method == 'POST':
#         return Response({"message": "Got some data!", "data": request.data})
#     return Response({"message": "Hello, world!"})

# class ViewDetail_Two(APIView):
#     def get(self, request, year=None, format=None) -> Response:
#         permission_classes = [permissions.IsAdminUser]
#         """ For listing out a single post, HTTP method: GET """
#         statistic = get_object_or_404(Statistic.objects.get(created_date=year))
#         serializer = SecondViewSerializer(statistic)
#         return Response(serializer.data,
#                         status=status.HTTP_200_OK)

class ViewDetail_Two(generics.ListAPIView):
    queryset = Statistic.objects.all()
    serializer_class = SecondViewSerializer
    permission_classes = [IsAdminUser]

    def detail(self, request, pk, year, month):
        day = 1
        # Note the use of `get_queryset()` instead of `self.queryset`
        # Payload.objects.filter(user=user_id, timestamp__range=[start_date, end_date]
        if request.method == 'GET':
            # statistic = Statistic.objects.get(pk=pk, created_date=year - month - day)
            statistic = Statistic.objects.get(pk=pk)
            serializer = FirstViewSerializer(statistic)
            return Response(serializer.data)
        pass



# class ArticleYearArchiveView(YearArchiveView):
#     queryset = Article.objects.all()
#     date_field = "pub_date"
#     make_object_list = True
#     allow_future = True


# class ViewDetail_Two(APIView):
#     def get(self, request, pk=None, format=None) -> Response:
#         permission_classes = [permissions.IsAdminUser]
#         """ For listing out a single post, HTTP method: GET """
#         statistic = get_object_or_404(Statistic.objects.all(), pk=pk)
#         serializer = SecondViewSerializer(statistic)
#         return Response(serializer.data,
#                         status=status.HTTP_200_OK)

# python3 manage.py shell


# class ViewDetail_Two(generics.ListAPIView):
#     def get_object(self, pk):
#         try:
#             return Statistic.objects.get(pk=pk)
#         except Statistic.DoesNotExist:
#             raise Http404
#
#     def get_object(self, year):
#         try:
#             return Statistic.objects.filter(date__year=year)
#         except Statistic.DoesNotExist:
#             raise Http404

    # def get(month=request.data['created_date'], post=None):
    #     data = request.data['created_date']
    #     if '2024' == request.created_date:
    #         return Response(status=status.HTTP_204_NO_CONTENT)
    #     else:
    #         return Response(status=status.HTTP_400_BAD_REQUEST)


    # serializer_class = SecondViewSerializer
    # permission_classes = [IsAdminUser]

# class ViewDetail_Three(APIView):
#     permission_classes = [IsAdminUser]
#
#     def get(self, request, pk):
#         statistic = Statistic.objects.get(client=pk)
#         serializer = ThirdViewSerializer(statistic)
#         return Response(serializer.data)


class ViewDetail_Three(generics.RetrieveAPIView):
    queryset = Statistic.objects.all()
    serializer_class = SecondViewSerializer
    permission_classes = [IsAdminUser]

    def detail(self, request, pk, year, month):
        day = 1
        # Note the use of `get_queryset()` instead of `self.queryset`
        # Payload.objects.filter(user=user_id, timestamp__range=[start_date, end_date]
        if request.method == 'GET':
            statistic = Statistic.objects.get(pk=pk, created_date=year - month - day)
            # statistic = Statistic.objects.get(pk=pk)
            serializer = ThirdViewSerializer(statistic)
            return Response(serializer.data)
        pass


# class SnippetList(APIView):
#     """
#     List all snippets, or create a new snippet.
#     """
#     def get(self, request, format=None):
#         snippets = Snippet.objects.all()
#         serializer = SnippetSerializer(snippets, many=True)
#         return Response(serializer.data)

# class SnippetDetail(APIView):
#     """
#     Retrieve, update or delete a snippet instance.
#     """
#     def get_object(self, pk):
#         try:
#             return Snippet.objects.get(pk=pk)
#         except Snippet.DoesNotExist:
#             raise Http404

# class SubjectListView(generics.ListAPIView):
#     queryset = Subject.objects.all()
#     serializer_class = SubjectSerializer

    # def get(month=request.data['created_date'], post=None):
    #     data = request.data['created_date']
    #     if '2024' == request.created_date:
    #         post.delete()
    #         return Response(status=status.HTTP_204_NO_CONTENT)
    #     else:
    #         return Response(status=status.HTTP_400_BAD_REQUEST)

# if request.method == 'GET':
#     ceh = request.GET['ceh']
#     uchastok = request.GET['uchastok']