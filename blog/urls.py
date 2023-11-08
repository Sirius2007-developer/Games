from django.urls import path
from .views import about, contact, index, product, remot, video, prodetailview
urlpatterns = [
    path('about/', about, name="about"),
    path('contact/', contact, name="contact"),
    path('index/', index, name="index"),
    path('product/', product, name="product"),
    path('remot/', remot, name="remot"),
    path('video/', video, name="video"),
    path('<int:id>', prodetailview, name='prodetail')
]