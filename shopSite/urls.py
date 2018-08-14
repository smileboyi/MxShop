"""shopSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
# from django.contrib import admin
from django.urls import path, include, re_path
import xadmin

from django.views.static import serve
from shopSite.settings import MEDIA_ROOT

from rest_framework.documentation import include_docs_urls

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_jwt.views import obtain_jwt_token

# from goods.view_base import GoodsListView
# from goods.views import GoodsListView
from goods.views import GoodsListViewSet,CategoryViewSet
from user_operation.views import UserFavViewset
from users.views import SmsCodeViewset,userViewset

from django.views.generic import TemplateView

from rest_framework.routers import DefaultRouter
router = DefaultRouter()

# DefaultRouter类会自动为我们创建the API root view，所以我们可以删除api_root
# 配置goods的url
router.register(r'goods', GoodsListViewSet,base_name='goods')
# 配置categorys的url
router.register(r'categorys', CategoryViewSet, base_name="categorys")
# 配置用户收藏的url
router.register(r'userfavs', UserFavViewset, base_name="userfavs")
# 配置codes的url
router.register(r'code', SmsCodeViewset, base_name="code")
# 配置users的url
router.register(r'usesr', userViewset, base_name="users")



urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('ueditor/', include('DjangoUeditor.urls')),
    # 添加rest_framework自带的登录窗口url
    # api-auth/login/和api-auth/logout/
    path('api-auth/',include('rest_framework.urls')),
    # 资源文件
    path('media/<path:path>',serve,{'document_root':MEDIA_ROOT}),
    # drf文档
    path('docs',include_docs_urls(title='drf文档')),

    # 商品列表页
    # path('goods/',GoodsListView.as_view(),name='goods-list')
    re_path('^', include(router.urls)),

    # 首页
    path('index/', TemplateView.as_view(template_name='index.html'),name='index'),

    # token认证
    path('api-token-auth/', obtain_auth_token),
    # jwt的token认证接口
    path('login/', obtain_jwt_token ),

]



"""
drf流程：
Models
  ↓
Serializers
  ↓
Viewsets
  ↓
Routers
  ↓
Urls
"""