from django.contrib import admin
from .models import Person
from .models import Drinks
from .models import DrinksCategory
from .models import Bookings
from .models import Menu
from .models import Book

from .models import Employee

from .models import Post

from .models import Rating
from .models import MenuItem,OrderItem,Order,Cart

# from .models import OrderItem
# from .models import Order
# from .models import Cart
from .models import Category

# Register your models here.
admin.site.register(Person)
admin.site.register(Drinks)
admin.site.register(DrinksCategory)
admin.site.register(Bookings)
admin.site.register(Menu)

admin.site.register(Employee)

admin.site.register(Post)
admin.site.register(Book)

admin.site.register(Rating)
admin.site.register(MenuItem)

admin.site.register(OrderItem)
admin.site.register(Order)
admin.site.register(Cart)

admin.site.register(Category)
