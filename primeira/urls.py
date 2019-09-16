from django.urls import path
from . import views

urlpatterns =[
    path('', views.primeira),
    path('produto/', views.produto_list),
    path('produto/create/', views.produto_form),
    path('produto/<int:produto_id>/', views.produto_show),
    path('excluir/<int:produto_id>/' ,views.excluir_produto),    
    path('editar/<int:produto_id>/' ,views.editar_produto)

]