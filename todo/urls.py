from django.urls import path

from .views import (
     todo_list,
     todo_create,
     todo_detail,
     todo_update,
     todo_delete
     )

app_name = 'todos'

urlpatterns = [
    path('', todo_list),
    path('create/', todo_create),
    path('<id>/', todo_detail), #burda id yazma nedenimiz url'de id çıkması için o objenin unique id'si
    path('<id>/update/', todo_update),
    path('<id>/delete/', todo_delete)

]