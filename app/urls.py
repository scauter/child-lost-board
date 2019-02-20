from django.urls import path

from . import views

# アプリケーションのルーティング設定

app_name = 'app'

urlpatterns = [
    path('info/edit/<int:info_id>', views.info_edit, name='info_edit'),
    path('info/del/<int:info_id>', views.info_del, name='info_del'),
    path('create/', views.create, name='create'),
    path('info/', views.info_list, name='info'),
    path('', views.index, name='index'),
]
