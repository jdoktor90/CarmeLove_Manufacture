from django.db.models import CharField, Model


class Category(Model):
    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'

    name = CharField(max_length=30)

    def __str__(self):
        return self.name

