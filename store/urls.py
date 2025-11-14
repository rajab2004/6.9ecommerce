from django.urls import path

from .views import CategoryView, ProductsView, ProductDetailView


urlpatterns = [
    path('categories/', CategoryView.as_view(), name='categories'),
    path('products/', ProductsView.as_view(), name='products'),
    path('products/<int:id>/', ProductDetailView.as_view(), name='detail'),
]

