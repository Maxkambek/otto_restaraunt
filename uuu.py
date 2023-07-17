import json
import requests
from main.models import Category, Product

url = "https://api-ru.iiko.services/api/1/nomenclature"

payload = json.dumps({
    "organizationId": "084fbb6f-e53b-4d4f-bd95-f17148a6d7de",
    "startRevision": 5
})
headers = {
    'Authorization': 'Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJBcGlMb2dpbklkIjoiZThjZWM4MmQtMjQzOS00ZmUxLThjMTAtNWQ1NmQ2NzdmNzE2IiwibmJmIjoxNjg5NDE3MDQxLCJleHAiOjE2ODk0MjA2NDEsImlhdCI6MTY4OTQxNzA0MSwiaXNzIjoiaWlrbyIsImF1ZCI6ImNsaWVudHMifQ.sahZ2x4PoKcL9VZawfCyesuw-E7uLl5EmDpAQbiOL-Y',
    'Content-Type': 'application/json'
}


def create_database():
    response = requests.request("POST", url, headers=headers, data=payload)
    res = dict(response.text)
    for i in res.groups:
        Category.objects.create(
            id=i.id,
            name=i.name,
            order=i.order,
            parent_group=i.parentGroup,
            isIncludedInMenu=i.isIncludedInMenu,
            isGroupModifier=i.isGroupModifier
        )
    for i in res.products:
        Product.objects.create(
            weight=i.weight,
            groupId=i.groupId,
            type=i.type,
            parentGroup=i.parentGroup,
            name=i.name,
            id=i.id
        )
    return print('hello')


create_database()
