from datetime import date

from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic.edit import CreateView

from .models import Product, Purchase

# Create your views here.
def index(request):
    products = Product.objects.all()
    context = {'products': products}
    return render(request, 'shop/index.html', context)


class PurchaseCreate(CreateView):
    model = Purchase
    fields = ['product', 'person', 'address', 'birthday', 'price']

    def form_valid(self, form):
        self.object = form.save()
        print(self.object.birthday, "1")
        print(date.today())
        price = Product.objects.get(pk=self.request.POST['product']).price
        if self.object.birthday == date.today():
            price = price * 0.9

        self.object.price = price
        self.object.save()
        if self.object.birthday == date.today():
            return HttpResponse(f'Спасибо за покупку, {self.object.person}, ваша цена со скидкой {self.object.price}!')
        else:
            return HttpResponse(f'Спасибо за покупку, {self.object.person}, ваша цена {self.object.price}!')