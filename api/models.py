from django.db import models
from django.contrib.postgres.fields import ArrayField


class News(models.Model):
    date = models.DateField(auto_now=True)
    header = models.CharField(max_length=255)
    main_text = models.TextField(max_length=100_000)
    sub_text_0 = models.TextField(max_length=50_000)
    images_0 = ArrayField(models.CharField(max_length=100, blank=True))
    sub_text_1 = models.TextField(max_length=50_000)
    images_1 = ArrayField(models.CharField(max_length=100, blank=True))
