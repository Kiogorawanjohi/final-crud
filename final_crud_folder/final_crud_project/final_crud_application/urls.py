from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('addvoter/', views.addvoter, name='addvoter'),
    path('viewvoters/', views.viewvoters, name='viewvoters'),
    path('editvoter{{/object.id}}/', views.editvoter, name='editvoter'),
    path('deletevoter/<int:id>/', views.deletevoter, name='deletevoter')
]