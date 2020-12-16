from django.db import models


class User(models.Model):

    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()
    password = models.CharField(max_length=60)

    def get_pass(self):
        return self.password


#  TODO: add here maybe class for movies




