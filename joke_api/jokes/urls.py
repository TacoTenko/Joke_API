from django.urls import path
from .views import joke_list, joke_detail, top_rated_jokes  # Use function-based views

urlpatterns = [
    path('jokes/', joke_list, name='joke-list-create'),  
    path('jokes/<int:joke_id>/', joke_detail, name='joke-detail'),
    path('jokes/top-rated/', top_rated_jokes, name='top-rated-jokes'),
]
