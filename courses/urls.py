from django.urls import path

from . import views

app_name = 'courses'
# angle bracket fillers are variable names
urlpatterns = [
    # screen for the lsting of course depts. to choose from
    # .../classes/
    path('', views.IndexView.as_view(), name='index'),
    # courses to choose from
    # e.g. .../classes/cse/
    path('<slug_dept>/', views.dept, name='department'),
    # path('<slug_dept>/', views.DeptView.as_view(), name='department'),

    # the course visualization (and maybe info)
    # e.g. .../classes/cse/143/
    path('<slug_dept>/<int:crs_num>/', views.vis_choose, name='visual_chooser'),
    path('<slug_dept>/<int:crs_num>/<int:yrqtr>', views.course_vis, name='course_visualization'),
    path('<slug_dept>/<int:crs_num>/select', views.selection, name='selection'),
]
