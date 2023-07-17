from django.db import models
import requests
import json


class Category(models.Model):
    id = models.CharField(max_length=123, primary_key=True, unique=True, db_index=True)
    name = models.CharField(max_length=555, null=True, blank=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    order = models.IntegerField(default=0)
    parent_group = models.CharField(max_length=123, null=True, blank=True)
    isIncludedInMenu = models.BooleanField(default=False)
    isGroupModifier = models.BooleanField(default=False)

    def __str__(self):
        return self.name


class Product(models.Model):
    id = models.CharField(max_length=123, primary_key=True, unique=True, db_index=True)
    weight = models.CharField(max_length=100, null=True, blank=True)
    groupId = models.CharField(max_length=123, null=True, blank=True)
    type = models.CharField(max_length=123, null=True, blank=True)
    parentGroup = models.CharField(max_length=123, null=True, blank=True)
    name = models.CharField(max_length=333, null=True, blank=True)

    def __str__(self):
        return self.name
