from django.urls import path,include
from .import views
urlpatterns = [
    path('register/',views.Registraion.as_view(),name='register'),
    path('change_user_data/<int:id>/',views.update_usuer_details,name='update_data'),
    path('login/', views.login.as_view(),name='login'),
    path('logout_page/',views.logoutpage,name='logoutpage'),
    path('logout/',views.logout_trigger,name='logout'),
    path('details/<int:id>/',views.PostDetailsView.as_view(),name='details'),
    path('edit_quantity/<int:id>/',views.edit_quantity_after_purchase,name='edit_quantity')
    
]
