from django.urls import path

from shop import views
app_name='shop'
urlpatterns = [
    path('',views.allproducts,name='allproducts'),
    path('<slug:c_slug>/',views.allproducts,name='product_by_category'),
    path('<slug:c_slug>/<slug:product_slug>/', views.productdetail, name='prod_cat_detail')

]