from django.urls import path,include
from .views import ArticleAPIView, ArticleDetails, GenericAPIVIEW, ArticleViewSet
from rest_framework.routers import DefaultRouter


########################################################################################################################

# Viewsets and Routers
router = DefaultRouter()
router.register('article',ArticleViewSet, basename='article')

########################################################################################################################

urlpatterns = [
    path('article/', ArticleAPIView.as_view()),
    path('generic/article/<int:id>/', GenericAPIVIEW.as_view()),
    path('detail/<int:id>/', ArticleDetails.as_view()),
    path('viewset/article', include(router.urls)),
    path('viewset/article/<int:pk>/', include(router.urls)),

]