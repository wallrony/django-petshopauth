from petshopauth.core import views
from django.urls import path

app_name = 'core'

urlpatterns = [
  path('pets', views.list_or_add),
  path('pets/<int:pet_id>', views.unique_pet),
  path('login', views.UserLoginApiView.as_view())
]