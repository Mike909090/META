from django.db import models 
from django.urls import reverse
from django.db import models
from django.contrib.auth.models import User

class Person(models.Model): 
    person_name = models.CharField(max_length=20) 
    email = models.EmailField() 
    phone = models.CharField(max_length=20) 
    age = models.CharField(max_length=20) 
    def __str__(self):
        return self.person_name
    
class DrinksCategory(models.Model):
    category_name = models.CharField(max_length=200)
    def __str__(self):
        return self.category_name
    
class Drinks(models.Model):
    drink = models.CharField(max_length=200)
    price = models.IntegerField()
    category_id = models.ForeignKey(DrinksCategory, on_delete=models.PROTECT, default=None)
    def __str__(self):
        return self.drink

class Bookings(models.Model):
    first_name = models.CharField(max_length = 200)
    last_name = models.CharField(max_length = 200)
    guest_count = models.IntegerField()
    reservation_date = models.DateField(auto_now=True)
    reservation_time = models.DateField(auto_now=True)
    comments = models.CharField(max_length=1000)
    def __str__(self):
      return self.first_name + ' ' + self.last_name

class Menu(models.Model):
   name = models.CharField(max_length=200) 
   price = models.IntegerField(null=False) 
   menu_item_description = models.TextField(max_length=1000, default='') 
   def __str__(self):
      return self.name


class Employee(models.Model):   
    name = models.CharField(max_length=100)   
    email = models.EmailField()   
    contact = models.CharField(max_length=15)   
    class Meta:   
        db_table = "Employee" 
    def __str__(self):
        return self.name


class Post(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    def __str__(self):
        return self.title
    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.pk)])


class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=5, decimal_places=2)

    class Meta:
        indexes = [
            models.Index(fields=['price']),
        ]

# class MenuItem(models.Model):
#     title = models.CharField(max_length=255)
#     price = models.DecimalField(max_digits=6, decimal_places=2)
#     inventory = models.SmallIntegerField()

class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menuitem_id =  models.SmallIntegerField()
    rating = models.SmallIntegerField()

class Category(models.Model):
    slug = models.SlugField()
    title = models.CharField(max_length=255, db_index=True)


# class MenuItem(models.Model):
#     title = models.CharField(max_length=255, db_index=True)
#     price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
#     featured = models.BooleanField(db_index=True)
#     category = models.ForeignKey(Category, on_delete=models.PROTECT)

class MenuItem(models.Model):
    item_name = models.CharField(max_length=255, db_index=True)
    category = models.ForeignKey(Category, on_delete=models.PROTECT)
    description = models.TextField(max_length=1000) 
    price = models.DecimalField(max_digits=6, decimal_places=2, db_index=True)
    featured = models.BooleanField(db_index=True)
    def __str__(self):
        return self.item_name
    

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    unit_price = models.DecimalField(max_digits=6, decimal_places=2)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    class Meta:
        unique_together = ('menuitem', 'user')


class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    delivery_crew = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name="delivery_crew", null=True)
    status = models.BooleanField(default=0, db_index=True)
    total = models.DecimalField(max_digits=6, decimal_places=2, default=0)
    date = models.DateField(db_index=True)


class OrderItem(models.Model):
    order = models.ForeignKey(
        Order, on_delete=models.CASCADE, related_name='order')
    menuitem = models.ForeignKey(MenuItem, on_delete=models.CASCADE)
    quantity = models.SmallIntegerField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    class Meta:
        unique_together = ('order', 'menuitem')
