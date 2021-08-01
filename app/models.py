from django.db import models
from django.contrib.auth.models import User

CHOOSE_STATE = (
    ('AL', 'Alabama'), ('AK', 'Alaska'), ('AS', 'American Samoa'), ('AZ', 'Arizona'), ('AR', 'Arkansas'), ('AA', 'Armed Forces Americas'), ('AE', 'Armed Forces Europe'), ('AP', 'Armed Forces Pacific'), ('CA', 'California'), ('CO', 'Colorado'), ('CT', 'Connecticut'), ('DE', 'Delaware'), ('DC', 'District of Columbia'), ('FM', 'Federated States of Micronesia'), ('FL', 'Florida'), ('GA', 'Georgia'), ('GU', 'Guam'), ('HI', 'Hawaii'), ('ID', 'Idaho'), ('IL', 'Illinois'), ('IN', 'Indiana'), ('IA', 'Iowa'), ('KS', 'Kansas'), ('KY', 'Kentucky'), ('LA', 'Louisiana'), ('ME', 'Maine'), ('MH', 'Marshall Islands'), ('MD', 'Maryland'), ('MA', 'Massachusetts'), ('MI', 'Michigan'), ('MN', 'Minnesota'), ('MS', 'Mississippi'), ('MO', 'Missouri'), ('MT', 'Montana'), ('NE', 'Nebraska'), ('NV', 'Nevada'), ('NH', 'New Hampshire'), ('NJ', 'New Jersey'), ('NM', 'New Mexico'), ('NY', 'New York'), ('NC', 'North Carolina'), ('ND', 'North Dakota'), ('MP', 'Northern Mariana Islands'), ('OH', 'Ohio'), ('OK', 'Oklahoma'), ('OR', 'Oregon'), ('PW', 'Palau'), ('PA', 'Pennsylvania'), ('PR', 'Puerto Rico'), ('RI', 'Rhode Island'), ('SC', 'South Carolina'), ('SD', 'South Dakota'), ('TN', 'Tennessee'), ('TX', 'Texas'), ('UT', 'Utah'), ('VT', 'Vermont'), ('VI', 'Virgin Islands'), ('VA', 'Virginia'), ('WA', 'Washington'), ('WV', 'West Virginia'), ('WI', 'Wisconsin'), ('WY', 'Wyoming')
)

CHOOSE_CATEGORY = (
    ('CS', 'Clothing and Shoes'),
    ('JA', 'Jewelry and Accessories'),
    ('HG', 'Home Goods'),
    ('E', 'Entertainment'),
    ('TECH', 'Technology'),
    ('TO', 'Toys'),
)

CHOOSE_ORDER_STATUS = (
    ('Order Received', 'Order Received'),
    ('Order Cancelled', 'Order Cancelled'),
    ('Packaging Done', 'Packaging Done'),
    ('On your way', 'On your way'),
    ('Delivered', 'Delivered'),
    ('Order Complete', 'Order Complete'),

    ('Return Initiated', 'Return Initiated'),
    ('Return Successful', 'Return Successful'),
    ('Refund Initiated', 'Refund Initiated'),
    ('Refund Successful', 'Refund Successful')
)

class Customer(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    street_address = models.CharField(max_length=150, null=False, default=' ')
    apt_house = models.CharField(max_length=50, null=False, default=' ')
    city = models.CharField(max_length=50, null=False)
    zipcode = models.IntegerField(null=False)
    state = models.CharField(choices=CHOOSE_STATE, max_length=10, null=False)
    phone_number = models.CharField(max_length=10, null=False)

    def __str__(self):
        return str(self.id)

class Product(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    category = models.CharField(choices=CHOOSE_CATEGORY, max_length=4)
    image = models.ImageField(upload_to='PRODUCT_IMAGES')

    def __str__(self):
        return str(self.id)

class CART(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return str(self.id)

class OrderPlaced(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    ordered_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(choices=CHOOSE_ORDER_STATUS,max_length=50, default='Order Received')

class ChatLinks(models.Model):
    user = models.CharField(max_length=100, default='xxx')
    room = models.CharField(max_length=100, default='xxx')
    link = models.CharField(max_length=250, default='xxx')




