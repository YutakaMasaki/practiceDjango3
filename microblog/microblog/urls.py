"""microblog URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

# 受け取ったリクエストがどこかを特定し、それに応答するviewsを繋ぐ役割
# リクエスト -> urls.py -> views -> テンプレート -> レスポンス -> ユーザー
# ページが多くなればなるほど、path関数で登録する数が多くなる

from django.contrib import admin
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from blog.views import BlogListView, BlogDetailView, BlogCreateView, BlogUpdateView, BlogDeleteView

urlpatterns = [
    #path('<URL>', views(関数), ニックネーム=None)
    #htto://localhost:8000/ : index
    path('', BlogListView.as_view(), name='index'),

    # http://localhost/20
    # pk = 20  (pk : primary key)
    path('<int:pk>', BlogDetailView.as_view(), name='detail'),

    path('create', BlogCreateView.as_view(), name='create'),

    path("<int:pk>/update", BlogUpdateView.as_view(), name="update"),
    path("<int:pk>/delete", BlogDeleteView.as_view(), name="delete"),
    
    path('admin/', admin.site.urls),

    path("login", LoginView.as_view(template_name="login.html"), name="login"),
    path("logout", LogoutView.as_view(template_name="logout.html"), name="logout")
]
