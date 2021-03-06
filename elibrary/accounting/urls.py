from django.urls import path
from django.conf.urls import url
from . import views


urlpatterns = [
    path('signup/',
         views.signup,
         name='signup'),
    url(r'^activate/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>[0-9A-Za-z]{1,13}-[0-9A-Za-z]{1,20})/$',
        views.activate,
        name='activate'),
    path('profile_details/',
         views.profile_detail,
         name='profile_details'),
    path('profile_edit/',
         views.profile_edit,
         name='profile_edit'),
    path('common_info/<str:unit_type>/',
         views.common_library_unit_info,
         name='common_info'),
    path('<str:unit_type>/<int:unit_number>/',
         views.library_unit_details,
         name='detailed_info'),
    path('edit/<str:unit_type>/<int:unit_number>/',
         views.library_unit_edit,
         name='edit_info'),
    path('add/<str:unit_type>/',
         views.library_unit_add,
         name='add_unit'),
    path('delete/<str:unit_type>/<int:unit_number>/',
         views.library_unit_delete,
         name='delete_library_unit'),
]
