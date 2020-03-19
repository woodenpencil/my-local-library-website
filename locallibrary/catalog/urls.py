from django.urls import path
from . import views

urlpatterns = [
	path("", views.index, name="index"),
	path("src_frg/<str:fragment>", views.search_fragment, name="src_frg")
]