from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import PostListView, PostDetailView, PostCreateView, PostUpdateView, PostDeleteView
from .views import EmployeeCreate, EmployeeList, EmployeeDetail, EmployeeUpdate, EmployeeDelete
from .views import success_view
from .views import delete_view
from rest_framework.routers import SimpleRouter
from rest_framework.routers import DefaultRouter

urlpatterns = [
        path('', views.home, name="home"),
        path('about/', views.about, name="about"),
        path('book/', views.book, name="book"), 
        path('menu/', views.menu, name="menu"),
        path('menu_item/<int:pk>/', views.display_menu_item, name="menu_item"),
        path('myname/', views.myName, name="myName"), 
        path('drinks/<str:drink_name>', views.drinks, name="drink_name"), 
        path('form/', views.index, name="forms"), 
        path('booking_forms/', views.index2, name="booking_forms"), 
        path('secret_menu/', views.secret_menu, name="secret_menu"),
        path('home_template/', views.home_template, name="home_template"), 
        path('about_template/', views.about_template, name="about_template"), 
        path('menu_template/', views.menu_template, name="menu_template"), 
        path('book_template/', views.book_template, name="book_template"), 
        path('employee/create/', EmployeeCreate.as_view(), name = 'EmployeeCreate'), 
        path('employee/list/', EmployeeList.as_view(), name = 'EmployeeList'), 
        path('employee/show/<int:pk>', EmployeeDetail.as_view(), name = 'EmployeeDetail'),
        path('employee/update/<int:pk>', EmployeeUpdate.as_view(), name = 'EmployeeUpdate') ,
        path('employee/delete/<int:pk>/', EmployeeDelete.as_view(), name='EmployeeDelete'),
        path('employees/success/', success_view, name='success'),
        path('employees/delete/', delete_view, name='success'),
        path('post/create/', PostCreateView.as_view(), name='post_create'),
        path('post/list/', PostListView.as_view(), name='post_list'),
        path('post/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
        path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post_edit'),
        path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post_delete'),
        path('originalbooks',views.books),
        path('originalbooks/<int:pk>',views.book),
        path('orders', views.Orders.listOrders),
        path('books', views.BookView1.as_view(
	{
	'get': 'list',
	'post': 'create',
	})
	),
        path('books/<int:pk>',views.BookView1.as_view(
	{
	'get': 'retrieve',
	'put': 'update',
	'patch': 'partial_update',
	'delete': 'destroy',
	})
	),
        path('books2', views.BookView2.as_view()),
        path('books2/<int:pk>', views.SingleBookView2.as_view()),
        path('ratings', views.RatingsView.as_view()),
        path('api/categories', views.CategoriesView.as_view()),
	path('api/menu-items', views.MenuItemsView.as_view()),
	path('api/menu-items/<int:pk>', views.SingleMenuItemView.as_view()),
	path('api/cart/menu-items', views.CartView.as_view()),
	path('api/orders', views.OrderView.as_view()),
	path('api/orders/<int:pk>', views.SingleOrderView.as_view()),
	path('api/groups/manager/users', views.GroupViewSet.as_view(
    	{'get': 'list', 'post': 'create', 'delete': 'destroy'})),
	path('api/groups/delivery-crew/users', views.DeliveryCrewViewSet.as_view(
    	{'get': 'list', 'post': 'create', 'delete': 'destroy'})),
        path('form_view',  views.form_view,  name='form_for_menu'),
        path('bookings', views.bookings, name='bookings'), 
      
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

router1 = SimpleRouter(trailing_slash=False)
router1.register('books1', views.BookView1, basename='books1')

router2 = DefaultRouter(trailing_slash=False)
router2.register('books2', views.BookView1, basename='books2')

# urlpatterns = router.urls

urlpatterns += router1.urls
urlpatterns += router2.urls
