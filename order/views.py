from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DeleteView, DetailView
from order.forms import OrderForms
from order.models import Order


def order_list(request):
    context = {
        "order_list": Order.objects.all()
    }
    return render(request, "order/list.html", context)


class OrderDetailView(DetailView):
    model = Order

    def get(self, *args, **kwargs):
        order = self.get_object()

        return super(OrderDetailView, self).get(*args, **kwargs)


class OrderCreateView(CreateView):
    model = Order
    fields = "__all__"
    template_name = "order/order_form.html"


class OrderUpdateView(UpdateView):
    model = Order
    fields = "__all__"

    def get_initial(self):
        queryset = super(OrderUpdateView, self).get_initial()
        return queryset


class OrderDeleteView(DeleteView):
    model = Order

# def order_create(request):
#     if request.method == "POST":
#         form = OrderForms(request.POST)
#     else:
#         form = OrderForms(request.POST)
#
#     return render(request, "order/order_form.html", {"form": form})
