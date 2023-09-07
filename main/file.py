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
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJBcGlMb2dpbklkIjoiZThjZWM4MmQtMjQzOS00ZmUxLThjMTAtNWQ1NmQ2NzdmNzE2IiwibmJmIjoxNjkwMDEwMDU5LCJleHAiOjE2OTAwMTM2NTksImlhdCI6MTY5MDAxMDA1OSwiaXNzIjoiaWlrbyIsImF1ZCI6ImNsaWVudHMifQ.bLhwg0gdvcV_MbCZPRtoH328cshe9aXl6_14Ghwm2e0',
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
                isGroupModifier=i['isGroupModifier'],
                isDeleted=i['isDeleted']
            )
        for i in res['products']:
            Product.objects.create(
                weight=i['weight'],
                groupId=i['groupId'],
                type=i['type'],
                parentGroup=i['parentGroup'],
                name=i['name'],
                id=i['id'],
                price=i['sizePrices'][0]['price']['currentPrice'],
                isDeleted=i['isDeleted'],
                measureUnit=i['measureUnit'],
                order=i['order']
            )
        return Response('Success')
