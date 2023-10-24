from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model

# Create your views here.
class FollowView(APIView):
	def post(self, request, user_pk):
		User = get_user_model()
		you = get_object_or_404(User, pk=user_pk)
		me = request.user
		
		if me in you.followers.all():
			you.followers.remove(me)
			return Response('unfollow', status=status.HTTP_200_OK)
		else:
			you.followers.add(me)
			return Response('follow', status=status.HTTP_200_OK)
		
	