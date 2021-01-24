from django.urls import path
from . import views
urlpatterns = [
    path('',views.load_index_page,name="laodindexpage")
]