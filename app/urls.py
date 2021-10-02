
from django.contrib import admin
from django.urls import path
from app.views import home , login , signup ,remove_task, memorize,signout,change_status


urlpatterns = [
    path('',home , name='home'),
    path('login/',login , name='login'),
    path('signup/',signup),
    path('memorize-task/',memorize),
    path('logout/',signout),
    path('removed-task/<int:id>/',remove_task),
    path('change-status/<int:id>/<str:status>',change_status)
]
