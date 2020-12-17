from django.db import models


class User(models.Model):

    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)
    email = models.EmailField()
    password = models.CharField(max_length=60)

    def get_pass(self):
        return self.password


class Movies(models.Model):

    title = models.CharField(max_length=60)
    actor = models.CharField(max_length=60)
    rate = models.FloatField()
    img = models.CharField(max_length=60)



class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    movie = models.ForeignKey(Movies, on_delete=models.CASCADE, null=True)





