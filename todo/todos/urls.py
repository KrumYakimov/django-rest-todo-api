from django.urls import path

from todo.todos import views

urlpatterns =[
    path("", views.TodoListCreateApiView.as_view(), name="todo-list-create"),
    path("<int:pk>/", views.TodoDetailView.as_view(), name="todo-detail"),
    path("categories/", views.CategoriesListView.as_view(), name="categories-list"),

]
