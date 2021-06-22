from complaints.views import homeView
from django.urls import path


from .views import homeView, detailView, createView, loginView, logoutView
urlpatterns = [
    path("", homeView, name="home"),
    path("logout", logoutView, name="logout"),
    path("complaints/<int:id>", detailView, name="detail"),
    path("create", createView, name="create"),
    path("login", loginView, name="login")
]
