from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from snippets import views
from rest_framework.schemas import  get_schema_view


schema_view = get_schema_view(title='Ornella Test API')


urlpatterns = [
    path('snippets/', views.SnippetList.as_view(), name='snippet-list'),
    path('snippets/<int:pk>/', views.SnippetDetail.as_view(), name='snippet-detail'),
    path('snippets/<int:pk>/highlight/',views.SnippetHighlight.as_view(), name='snippet-highlight'),
    path('users/', views.UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', views.UserDetail.as_view(), name='user-detail'),
    path('', views.api_root),
    path('schema/', schema_view),
]

urlpatterns = format_suffix_patterns(urlpatterns)


