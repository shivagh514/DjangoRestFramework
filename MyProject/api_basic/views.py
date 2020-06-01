from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from .models import Article
from .serializers import ArticleSerializer
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

class articleListClass(APIView):

    def get(self, request):
            article=Article.objects.all()
            serializer=ArticleSerializer(article, many=True)
            return Response(serializer.data)


    def post(self, request):
            serializer=ArticleSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class articleDetailClass(APIView):

    def is_exist(self, pk):
        try:
            article=Article.objects.get(pk=pk)
            return article
        except Article.DoesNotExist:
            return HttpResponse(status=404)

    def get(self, request, pk):
        article=self.is_exist(pk)
        serializer=ArticleSerializer(article)
        return Response(serializer.data)

    def put(self, request, pk):
        article=self.is_exist(pk)
        serializer=ArticleSerializer(article,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        article=self.is_exist(pk)
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)









# # Create your views here.
# @api_view(['GET', 'POST'])
# def article_list(request):
#     if request.method == 'GET':
#         article=Article.objects.all()
#         serializer = ArticleSerializer(article, many=True)
#         return Response(serializer.data)

#     elif request.method=='POST':
#         serializer = ArticleSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# @api_view(['GET', 'PUT', 'DELETE'])
# def article_detail(request, pk):
#     try:
#         article=Article.objects.get(pk=pk)
#     except Article.DoesNotExist:
#         return HttpResponse(status=404)
    
#     if request.method == 'GET':
#         serializer=ArticleSerializer(article)
#         return Response(serializer.data, status=status.HTTP_200_OK)
    
#     elif request.method == 'PUT':
#         serializer=ArticleSerializer(article, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_202_ACCEPTED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     elif request.method == 'DELETE':
#         article.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)





