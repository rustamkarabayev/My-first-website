# from django.shortcuts import render
# from rest_framework.response import Response
# from rest_framework.views import APIView
# from rest_framework import status
# from permissions import OnlyForAdmin, ForAllUsersPermission
# from .models import Team
# from .serializers import TeamSerializer
#
#
# class TeamDetail(APIView):
#     def get(self, request):
#         obj = Team.objects.all()
#         serializer = TeamSerializer(obj, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def post(self, request):
#         serializer = TeamSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.data, status=status.HTTP_400_BAD_REQUEST)
#
#     permission_classes = (ForAllUsersPermission,)
#
#
# class TeamInfo(APIView):
#     def get(self, request, id):
#         try:
#             obj = Team.objects.get(id=id)
#
#         except Team.DoesNotExist:
#             message = {"message": "not found"}
#             return Response(message, status=status.HTTP_404_NOT_FOUND)
#
#         serializer = TeamSerializer(obj)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def patch(self, request, id):
#         try:
#             obj = Team.objects.get(id=id)
#
#         except Team.DoesNotExist:
#             message = {"message": "not found error"}
#             return Response(message, status=status.HTTP_404_NOT_FOUND)
#
#         serializer = TeamSerializer(obj, data=request.data, partial=True)
#
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_205_RESET_CONTENT)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
#
#     def delete(self, request, id):
#         try:
#             obj = Team.objects.get(id=id)
#
#         except Team.DoesNotExist:
#             message = {"message": "not found"}
#             return Response(message, status=status.HTTP_404_NOT_FOUND)
#
#         obj.delete()
#         return Response({"message": "deleted"}, status=status.HTTP_204_NO_CONTENT)
#
#     permission_classes = (OnlyForAdmin,)


from django.http import HttpResponse
from django.shortcuts import render, redirect
from rest_framework import generics

from .forms import ReviewForm
from .models import Team, Services, Review
from .permissions import OnlyForAdmin, ForAllUsersPermission
from .serializers import TeamSerializer, ServicesSerializer, ReviewSerializer


class TeamDetail(generics.ListCreateAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = (ForAllUsersPermission,)


class TeamInfo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Team.objects.all()
    serializer_class = TeamSerializer
    permission_classes = (OnlyForAdmin,)


class ServicesList(generics.ListCreateAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    permission_classes = (ForAllUsersPermission,)


class ServicesUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Services.objects.all()
    serializer_class = ServicesSerializer
    permission_classes = (OnlyForAdmin,)


class ReviewList(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (ForAllUsersPermission,)


class ReviewUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = (OnlyForAdmin,)


def about(request):
    return render(request, 'about.html')


def home(request):
    form = ReviewForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('/')
    services = Services.objects.all()
    staff = Team.objects.all()
    return render(request, 'index.html', context={"services": services, "staff": staff, "form": form})


def getService(request, id):
    services = Services.objects.get(id=id)
    return render(request, "services.html", context={"service": services})
