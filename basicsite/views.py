from django.shortcuts import render_to_response
from ab_test.models import Test


def register(request):
    Test.goal(request)
    return render_to_response('registered.html')
