from mycv.views import home_view,details,blogdetails,covid,tiwtter,delivery
from django.urls import path

urlpatterns = [


    path('details/',details,name='details'),
    path('blogdetails/',blogdetails,name='blogdetails'),
    path('covid/',covid,name='covid'),
    path('tiwtter/',tiwtter,name='tiwtter'),
    path('delivery/',delivery,name='delivery'),




]