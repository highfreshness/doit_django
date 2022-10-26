from django.urls import path
from .views import PostList, PostDetail

urlpatterns = [
    # path('', views.index, name='index'), # FBV 방식의 call
    path('', PostList.as_view(), name='post_list'),
    path('<int:pk>/', PostDetail.as_view(), name="post_detail"),
]
