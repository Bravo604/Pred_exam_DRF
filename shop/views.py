from django.db import IntegrityError
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, get_object_or_404
from .serializers import CategorySerializer, ItemSerializer, OrderSerializer
from rest_framework.authentication import SessionAuthentication, TokenAuthentication

from .models import Category, Item, Order, Profile
from .permissions import IsAuthorPermission


class CategoryViewSet(ModelViewSet):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()
    authentication_classes = [SessionAuthentication, TokenAuthentication, ]
    # permission_classes = [IsAuthorPermission, ]

    # def get_queryset(self):
    #     return self.queryset.filter(ca=self.kwargs['item_id'])

    # def perform_create(self, serializer):
    #     profile = Profile.objects.filter(is_sender=True)
    #     if profile:
    #         serializer.save()


class ItemListCreateAPIView(ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication, ]
    # permission_classes = [IsAuthorPermission, ]

    def get_queryset(self):
        return self.queryset.filter(category_id=self.kwargs['category_id'])

    def perform_create(self, serializer):
        serializer.save()


class ItemRetrieveDestroyUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    authentication_classes = [SessionAuthentication, TokenAuthentication, ]
    # permission_classes = [IsAuthorPermission, ]


class OrderListCreateAPIView(ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

    # def get_queryset(self):
    #     return self.queryset.filter(item_id=self.kwargs['item_id'])
    #
    # def perform_create(self, serializer):
    #     profile = Profile.objects.filter(is_sender=True)
    #     if profile:
    #         serializer.save()


class OrderRetrieveDestroyUpdateAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
