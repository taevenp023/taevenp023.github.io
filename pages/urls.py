from django.urls import path
from .views import home_page_view, about_page_view, product_page_view

urlpatterns = [
    path("about/", about_page_view.as_view(), name="about"),
    path("", home_page_view, name="home"),
    path("products/", product_page_view.as_view(), name="products"),
]
