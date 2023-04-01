from django.urls import path
from social_cards import views

urlpatterns = [
    path("", views.api_root),
    path("cards/", views.CardList.as_view(), name="card-list"),
    path("cards/<int:pk>/", views.CardDetail.as_view(), name='card-detail'),
    path('cards/search/', views.CardSearch.as_view(), name='card-search'),
    path('cards/create/', views.CardCreate.as_view(), name='card-create'),
    path('users/', views.UserList.as_view(), name="users"),
]
