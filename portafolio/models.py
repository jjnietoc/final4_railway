from django.db import models

class Portfolio(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=200)
    tags = models.CharField(max_length=100)
    url = models.CharField(max_length=200)
    photo = models.ImageField(default=0, upload_to='fotos')
    class Meta:
        db_table = 'portafolio_portfolio'

class ip(models.Model):
    pub_date = models.DateTimeField('date published')
    ip_address = models.GenericIPAddressField()