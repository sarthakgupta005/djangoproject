from django.shortcuts import render
from django.http import HttpResponse
import boto3
# Create your views here.
def myfunc(request):
    return render(request, 'home_page.html', {})


def myfunc1(request):
    ec2 = boto3.client('ec2')
    response = ec2.describe_instances(InstanceIds=['i-096af0b8efeddbe75'])
    print(response)
    return HttpResponse(response)
