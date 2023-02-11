from django.urls import path
from posts.views import HomePageView, MessageCreateView, MessageDeleteView, MessageDetailView, MessageListView, AddComment, MessageUpdateView
from . import views

urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("messages/create/", MessageCreateView.as_view(), name="message_create"),
    path("messages/", MessageListView.as_view(), name="messages"),
    path("messages/<int:pk>/", MessageDetailView.as_view(), name="message_detail"),
    path("add comments/", AddComment.as_view(), name="add comments"),
    path("messages/<int:pk>/delete/", MessageDeleteView.as_view(), name="messages_delete"),
    path("messages/<int:pk>/update/", MessageUpdateView.as_view(), name="messages_edit"),
    path("likes/<int:pk>/", views.add_likes, name="likes")
]