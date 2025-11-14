import json

from django.views import View
from django.http import HttpRequest, JsonResponse

from .models import Category, Product


class CategoryView(View):
    
    def get(self, request: HttpRequest) -> JsonResponse:
        
        categories = list(Category.objects.values('id', 'name'))
        # for category in Category.objects.all():
        #     categories.append(category.name)

        return JsonResponse(data={'categories': categories})
    

class ProductsView(View):
    
    def get(self, request: HttpRequest) -> JsonResponse:
        params = request.GET

        products = Product.objects.all()

        category = params.get('category')
        if category:
            category = Category.objects.get(name=category)
            products = category.products

        products = list(products.values('id', 'name', 'price'))

        return JsonResponse(data={'products': products})

    def post(self, request: HttpRequest) -> JsonResponse:
        pass


class ProductDetailView(View):

    def get(self, request: HttpRequest, id: int) -> JsonResponse:
        pass

    def put(self, request: HttpRequest, id: int) -> JsonResponse:
        pass

