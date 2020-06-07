from django.urls import path
from .views import home_page, register, login, cards, user_home,card_desc, card_delete, send_mail, user_info

urlpatterns = [
    path('', home_page, name='home_page'),
    path('register/', register, name="register"),
    path('login/', login, name="login"),
    path('user/<int:my_id>', user_home, name='user_home'),
    path('user/<int:my_id>/cards', cards, name='cards'),
    path('user/<int:my_id>/cards/<int:card_id>', card_desc, name='card_desc'),
    path('user/<int:my_id>/card_del/<int:card_id>', card_delete, name='card_delete'),
    path('user/<int:my_id>/send_mail/<int:card_id>', send_mail, name='send_mail'),
    path('user/<int:my_id>/user_info',user_info,name='user_info'),
]
