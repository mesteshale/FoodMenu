from .import views
from django.urls import path
app_name = 'food'
urlpatterns = [
    #/food
    path('', views.index,name='index'),
    #/food/item
    path('item/',views.item,name='item'),
    #/food/id
    path('<int:item_id>/',views.detail,name='detail'),
    #create item 
    path('create',views.create_item,name='create_item'),
    #update item
    path('update/<int:id>/',views.update_item,name='update_item'),
    #delete item
    path('delete/<int:id>/',views.delete_item,name='delete_item')
  ] 