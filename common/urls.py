from django.urls import path
from django.contrib.auth import views as auth_views

from .views import *

app_name = 'common'

urlpatterns = [
    path('', index, name='index'),

    # 회원가입
    # path('signup/', signup, name='signup'),
    path('signup/', SignupView.as_view(), name='signup'),  # Json으로 회원가입 (react에서 사용)
    path('signup/comp/', signup_complete, name='signup_complete'),

    # 일반 로그인
    # path('login/', login_main, name='login_main'),
    path('login/', LoginView.as_view(), name='login_main'),  # Json으로 로그인 (react에서 사용)
    # path('login/', login_with_cookie, name='login_main'),  # Cookie 설정(HTML ver)
    path('logout/', logout_main, name='logout_main'),

    # 아이디 중복 확인
    path('signup/check/id/', CheckID.as_view(), name='duplicate_id_check'),
    # 이메일 인증번호 확인
    path('signup/auth/email/', EmailAuth.as_view(), name='auth_email'),
    path('signup/auth/email/comp/', EmailAuthComplete.as_view(), name='auth_email_complete'),
]