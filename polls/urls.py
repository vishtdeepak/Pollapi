from django.urls import path
from rest_framework import routers
from .views import poll_detail, poll_list
from .apiviews import  ChoiceList, CreateVote, UserCreate, LoginView
from rest_framework import routers
from .apiviews import PollViewSet
from rest_framework.authtoken import views

router = routers.DefaultRouter()
router.register('polls', PollViewSet, basename='polls')

urlpatterns = [

    path('polls/<int:pk>/choices/', ChoiceList.as_view(),name="choice_list"),
    path('polls/<int:pk>/choices/<int:choice_pk>/vote/', CreateVote.as_view(),name="create_vote"),
    path('users/', UserCreate.as_view(), name='user_create'),
    path('login/',LoginView.as_view(), name='login'),
    
]
urlpatterns += router.urls