from .import views
from django.urls import path
app_name = 'food'
urlpatterns = [
    #/food
   # path('', views.index,name='index'),
    path('',views.IndexClassView.as_view(),name='index'),	
    #/food/item
    path('item/',views.item,name='item'),
    #/food/id
    #path('<int:item_id>/',views.detail,name='detail'),
    path('<int:pk>/',views.DetailView.as_view(),name='detail'),
    #create item 
    path('create',views.CreateItem.as_view(),name='create_item'),
    #update item
    path('update/<int:id>/',views.update_item,name='update_item'),
    #delete item
    path('delete/<int:id>/',views.delete_item,name='delete_item')
    
  ] 