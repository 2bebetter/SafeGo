from django.contrib import admin
from django.conf.urls import include
from django.urls import path
from routes import views

urlpatterns = [
    path('riskIndex/', views.risk_index().post)
]