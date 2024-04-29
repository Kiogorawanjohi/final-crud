from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('addvoter/', views.addvoter, name='addvoter'),
    path('viewvoters/', views.viewvoters, name='viewvoters'),
    path('editvoter/<int:id>/', views.editvoter, name='editvoter'),
    path('updatevoter/<int:id>/', views.updatevoter, name='updatevoter'),
    path('deletevoter/<int:id>/', views.deletevoter, name='deletevoter'),
]