from django.db import models
from django.utils import timezone

# Create your models here.

class Accounts(models.Model):
    name = models.CharField(max_length=24)
    password = models.CharField(max_length=24)
    join_date = models.DateTimeField()

    def join(self):
        self.join_date = timezone.now()
        self.save()

    def __str__(self):
        return "%s, joined : %s" % (self.name, self.join_date)


class Photos(models.Model):
    description = models.CharField(max_length=144)
    like_count = models.BigIntegerField()
    post_date = models.DateTimeField()
    author = models.ForeignKey(Accounts, on_delete=models.CASCADE)

class Comments(models.Model):
    content = models.CharField(max_length=144)
    author = models.ForeignKey(Accounts, on_delete=models.CASCADE)
    photo = models.ForeignKey(Photos, on_delete=models.CASCADE)



