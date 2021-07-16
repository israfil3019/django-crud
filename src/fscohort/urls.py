from django.urls import path
from .views import StudentCreate, StudentDelete, StudentDetail, StudentList, StudentUpdate, student_update, HomeView
# from django.views.generic import TemplateView

urlpatterns = [
    # path("", home_page, name="home"),
    # path("", TemplateView.as_view(template_name="fscohort/home.html"), name="home"),
    path("", HomeView.as_view(), name="home"),
    # path("list/", student_list, name="list"),
    path("list/", StudentList.as_view(), name="list"),
    # path("add/", student_add, name="add"),
    path("add/", StudentCreate.as_view(), name="add"),
    # path("<int:id>/", student_detail, name="detail"),     # it use id; we can change it from detail.py
    # must call with slug or object pk; //
    path("<int:pk>/", StudentDetail.as_view(), name="detail"),
    path("<int:id>/update/", student_update, name="update"),
    # path("<int:id>/update/", StudentUpdate.as_view(), name="update"),
    # path("<int:id>/delete/", student_delete, name="delete"),
    path("<int:id>/delete/", StudentDelete.as_view(), name="delete"),
]
