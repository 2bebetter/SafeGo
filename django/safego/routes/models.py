from django.shortcuts import render
from django.http import HttpResponse
from django.db import models

class Question(models.Model):
    address =models.TextField(blank=False, null=False)
    city =models.TextField(blank=True, null=True)
    body = models.TextField(blank=False, null=False)
