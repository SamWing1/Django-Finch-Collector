from django.urls import path
from . import views 

urlpatterns = [
    path('', views.about, name='about'),
    path('about/', views.about, name='about'),
    path('finches/', views.FinchList.as_view(), name='index'),
    path('finches/<int:finch_id>/', views.finches_detail, name='detail'),
    path('finches/create/', views.FinchCreate.as_view(), name='finches_create'),
    path('finches/<int:pk>/update', views.FinchUpdate.as_view(), name='finches_update'),
    path('finches/<int:pk>/delete', views.FinchDelete.as_view(), name='finches_delete'),
    path('finches/<int:finch_id>/add_sighting/', views.add_sighting, name='add_sighting'),
    path('tags/', views.TagList.as_view(), name='tags_index'),
    path('tags/<int:pk>/', views.TagDetail.as_view(), name='tags_detail'),
    path('tags/create/', views.TagCreate.as_view(), name='tags_create'),
    path('tags/<int:pk>/update', views.TagUpdate.as_view(), name='tags_update'),
    path('tags/<int:pk>/delete', views.TagDelete.as_view(), name='tags_delete'),
    path('finches/<int:finch_id>/assoc_tag/<int:tag_id>/', views.assoc_tag, name='assoc_tag'),
]