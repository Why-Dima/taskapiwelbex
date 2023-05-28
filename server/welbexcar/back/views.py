from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import CarSerializer, CargoSerializer
from rest_framework import status
from rest_framework.response import Response

from geopy.distance import geodesic
from .models import *
import threading
import random


def car_location():
    threading.Timer(180.0, car_location).start()
    for car in Car.objects.all():    
        car.location = Location.objects.get(id=random.randrange(33788))
        car.save()

car_location()


class CargoAPIView(APIView):    
    def get(self, request, pk):
        cargo = Cargo.objects.get(id=pk)
        list_cars = Car.objects.all()
        l1 = cargo.loc_pick_up.lat
        l2 = cargo.loc_pick_up.lng
        l = (l1, l2)
        return Response((CargoSerializer(cargo).data, 
                        [(i.number, geodesic(l,(i.location.lat, i.location.lng)).mi) for i in list_cars]))


class CargoAPICreate(APIView):
    def get(self, request):
        query = Cargo.objects.all().values()
        cars = []
        for cargo in Cargo.objects.all():
            amount_car = 0
            for car in Car.objects.all():
                if geodesic((cargo.loc_pick_up.lat, cargo.loc_pick_up.lng),(car.location.lat, car.location.lng)).mi <= 450:
                    amount_car += 1
            cars.append(amount_car)
        return Response((list(query), cars))
    
    def post(self, request):
        serializer = CargoSerializer(data=request.data)
        serializer.initial_data['loc_pick_up'] = Location.objects.get(zip=request.data['zip']).id
        serializer.initial_data['loc_delivery'] = Location.objects.get(zip=request.data['zip']).id
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
    def put(self, request, **kwargs):
        pk = kwargs.get('pk')
        instance = Cargo.objects.get(pk=pk)
        serializer = CargoSerializer(data=request.data ,instance=instance)
        serializer.initial_data['loc_pick_up'] = Location.objects.get(zip=request.data['zip']).id
        serializer.initial_data['loc_delivery'] = Location.objects.get(zip=request.data['zip']).id
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    def delete(self, request, **kwargs):
        pk = kwargs.get('pk')
        cargo = Cargo.objects.get(pk=pk)
        cargo.delete()
        return Response('Cargo delete')


class CarAPIUpdate(APIView):
    def get(self, request, pk):
        car = Car.objects.get(id=pk)
        return Response(CarSerializer(car).data)
        
    def put(self, request, **kwarg):
        pk = kwarg.get('pk')
        instance = Car.objects.get(pk=pk)
        request.data['location'] = Location.objects.get(zip=request.data['zip']).id
        serializer = CarSerializer(data=request.data, instance=instance)
        serializer.is_valid(raise_exception=True)
        serializer.save()      
        return Response(serializer.data)

