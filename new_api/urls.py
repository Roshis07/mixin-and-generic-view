
from django.urls import path, include
from .views import user_list,item_list,user_details,item_details,CustomerReviewList,CustomerReviewDetail

urlpatterns = [
    path('users/',user_list.as_view() , name="users"),
    path('items/',item_list.as_view() , name="items"),
    path('user/<int:pk>/',user_details.as_view() , name="users_details"),
    path('item/<int:pk>/',item_details.as_view(), name="items_details"),
    path('reviews/', CustomerReviewList.as_view(), name='review-list'),
    path('reviews/<int:pk>/', CustomerReviewDetail.as_view(), name='review-detail'),
]
