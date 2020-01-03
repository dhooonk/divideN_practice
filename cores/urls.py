from django.urls import path
from moneybooks import views as moneybook_views

app_name = "cores"

urlpatterns = [path("", moneybook_views.all_moneybooks, name="home")]
