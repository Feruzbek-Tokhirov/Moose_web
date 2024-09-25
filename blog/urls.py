from django.urls import path
from .views import index, about, article, contact

urlpatterns = [
    path("", index),
    path("about/", about),
    path("article/", article),
    path("contact/", contact)
]
