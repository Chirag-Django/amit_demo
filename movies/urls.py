from django.urls import path
from .views import index_func,add_movie,movie_delete,movie_update,MovieList,MovieDetail

urlpatterns = [
    path('home/',index_func,name='home'),
    # path('list/',movie_list,name='movie_list'),
    path('list/',MovieList.as_view(),name='movie_list'),
    path('detail/<int:pk>/',MovieDetail.as_view(),name='movie_detail'),
    path('add/',add_movie,name='create_movie'),
    path('delete/<int:id>/',movie_delete,name='movie_destroy'),
    path('update/<int:id>/',movie_update,name='update_movie')
]
