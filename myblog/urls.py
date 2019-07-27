from django.urls import path
from myblog.views import list_view, detail_view, get_genres, stub_view

urlpatterns = [
    path('', list_view, name="blog_index"),
    path('myblog/<int:post_id>/', detail_view, name="blog_detail"),
    path('myblog/<genre>/', get_genres, name="genre_index"),

]