from django.urls import path
from .views import Statusapi, Statuslist, StatusCreateapi, StatusUpdateApi,\
                 StatusDetailsApi, StatusDeleteApi
app_name = 'status'

urlpatterns = [
    path('status/', Statusapi.as_view()),
    path('status/list/', Statuslist.as_view()),
    path('status/create/', StatusCreateapi.as_view()),
    path('status/update/<pk>', StatusUpdateApi.as_view()),
    path('status/detail/<pk>', StatusDetailsApi.as_view()),
    path('status/delete/<pk>', StatusDeleteApi.as_view()),
]



