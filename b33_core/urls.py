from django.urls import path
from django.views.generic import TemplateView
from b33_core import views as bv

urlpatterns = [
    path('insights/table/', bv.table_view, name="table"),
    path('insights/', bv.insight_view, name="insights"),
    path('', bv.search_view, name="search"),
]
