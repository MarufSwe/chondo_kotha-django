from django.db import models


class NameBn(models.Model):
    name = models.CharField(max_length=25)
    bn_name = models.CharField(max_length=25)

    def __str__(self):
        self.name

    class Meta:
        abstract = True


# Create your models here.
class Division(NameBn):
    url = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class District(NameBn):
    lat = models.CharField(max_length=15, null=True)
    lon = models.CharField(max_length=15, null=True)
    url = models.CharField(max_length=50, null=True)
    division = models.ForeignKey(Division, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.name


class Category(NameBn):

    def __str__(self):
        return self.name


class ChondoKotha(models.Model):
    title = models.CharField(max_length=30)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True, blank=True)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.title
