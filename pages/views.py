from typing import Any
from django.shortcuts import render
from django.views.generic import TemplateView


def home_page_view(request):
    context = {
        "inventory_list": ["Widget 1", "Widget 2", "Widget 3"],
        "greeting": "Thank You for Visiting.",
    }
    return render(request, "home.html", context)


class about_page_view(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contact_address"] = "123 Main St."
        context["phone_number"] = "555-555-5555"
        return context


class product_page_view(TemplateView):
    template_name = "products.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["products"] = ["Product 1", "Product 2", "Product 3", "Product 4"]
        return context
