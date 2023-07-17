import json

import requests
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Category, Product
from rest_framework import generics

url = "https://api-ru.iiko.services/api/1/nomenclature"

payload = json.dumps({
    "organizationId": "084fbb6f-e53b-4d4f-bd95-f17148a6d7de",
    "startRevision": 5
})
headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJBcGlMb2dpbklkIjoiZThjZWM4MmQtMjQzOS00ZmUxLThjMTAtNWQ1NmQ2NzdmNzE2IiwibmJmIjoxNjg5NDE3MDQxLCJleHAiOjE2ODk0MjA2NDEsImlhdCI6MTY4OTQxNzA0MSwiaXNzIjoiaWlrbyIsImF1ZCI6ImNsaWVudHMifQ.sahZ2x4PoKcL9VZawfCyesuw-E7uLl5EmDpAQbiOL-Y',
    'Content-Type': 'application/json'
}


class API(APIView):
    def get(self, request, *args, **kwargs):
        res = requests.request("POST", url, headers=headers, data=payload)
        res = res.json()
        for i in res['groups']:
            Category.objects.create(
                id=i['id'],
                name=i['name'],
                order=i['order'],
                parent_group=i['parentGroup'],
                isIncludedInMenu=i['isIncludedInMenu'],
                isGroupModifier=i['isGroupModifier']
            )
        for i in res['products']:
            Product.objects.create(
                weight=i['weight'],
                groupId=i['groupId'],
                type=i['type'],
                parentGroup=i['parentGroup'],
                name=i['name'],
                id=i['id']
            )
        return Response('Success')
