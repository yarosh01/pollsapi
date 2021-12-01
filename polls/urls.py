from django.urls import path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework.documentation import include_docs_urls

from .apiviews import ChoiceList, CreateVote, PollViewSet, UserCreate, LoginView


router = DefaultRouter()
router.register('polls', PollViewSet, basename='polls')

urlpatterns = [
    path("login/", views.obtain_auth_token, name="login"),
    path("polls/<int:pk>/choices/", ChoiceList.as_view(), name="choice_list"),
    path("polls/<int:pk>/choices/<int:choice_pk>/vote/", CreateVote.as_view(), name="create_vote"),
    path("users/", UserCreate.as_view(), name="user_create"),
    path(r'docs/', include_docs_urls(title='Polls API')),
]

urlpatterns += router.urls
