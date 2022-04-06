
from django.urls import path
from blogapp import views

urlpatterns = [
    path("list/" , views.posts_list_view),
    path("user/" , views.register_user),
    path('create/blog/' , views.create_new_blog_view),
    path('detail/blog/<int:id>/' , views.detail_blog_view),
    path('edit/<int:id>/' , views.update_view),
    path('delete/<int:id>/' , views.delete_view)

]
