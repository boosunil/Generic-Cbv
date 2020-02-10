from django.urls import path
from newapp.views import MyView, MyListView, MyDetailView, MyCreateView, MyUpdateView, MyDeleteView

urlpatterns = [
    path('page1', MyView.as_view()),
    path('', MyListView.as_view(), name='list-view'),
    path('page3/<int:pk>/', MyDetailView.as_view(), name='detail-view'),
    path('page4', MyCreateView.as_view(), name='create-view'),
    path('page5/<int:pk>/', MyUpdateView.as_view(), name='update-view'),
    path('page6/<int:pk>/', MyDeleteView.as_view(), name='delete-view')
]
