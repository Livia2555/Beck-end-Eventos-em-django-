from django.urls import path
from . import views

urlpatterns =[
    path('eventos/',views.read_eventos, name='read_eventos'),
    path('eventos/criar/', views.create_evento , name='create_evento'),
    path('eventos/atualizar/<int:pk>', views.update_evento , name='update_evento'),
    path('eventos/deletar/<int:pk>', views.delete_evento , name='delete_evento'),
    path('eventos/proximos/', views.proximo_eventos , name='proximo_eventos'),
    path('eventos/<int:pk>', views.read_evento )
]