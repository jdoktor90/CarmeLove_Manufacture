from django.contrib.auth.models import User
from django.db.models import BooleanField, CASCADE, CharField, DecimalField, \
    FloatField, ForeignKey, ImageField, \
    IntegerField, Model, OneToOneField, SET_NULL, TextField


class Customer(Model):
    user = OneToOneField(User, null=True, blank=True, on_delete=CASCADE)
    name = CharField(max_length=70, null=True)
    email = CharField(max_length=40, null=True)

    def __str__(self):
        return self.name


class Category(Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = CharField(max_length=30)

    def __str__(self):
        return self.name


MEASURE_TYPE = (
    (1, 'By Weight'),
    (2, 'By Quantity')
)

PACKAGE_SIZE = (
    (1, '100 gr'),
    (2, '250 gr'),
    (3, '500 gr'),
    (4, '1 kg'),
    (5, '1'),
    (6, '4'),
    (7, '6'),
    (8, '12'),
    (9, '24')
)


class Product(Model):
    class Meta:
        verbose_name = 'Product'
        verbose_name_plural = 'Products'

    name = CharField(max_length=70)
    category = ForeignKey(Category, on_delete=SET_NULL, null=True, blank=True)
    measure = IntegerField(verbose_name='Kind of measure', choices=MEASURE_TYPE)
    package = IntegerField(verbose_name='Package size', choices=PACKAGE_SIZE)
    description = TextField(max_length=700, null=False, blank=False)
    price = DecimalField(max_digits=6, decimal_places=2)
    availability = IntegerField(null=False, blank=False)
    weight = FloatField(null=True, blank=True)
    digital = BooleanField(default=False, null=True, blank=True)
    image = ImageField(null=True, blank=True)

    def __str__(self):
        return self.name

    @property
    def imageURL(self):
        if self.image:
            url = self.image.url
        else:
            url = ''
        return url

