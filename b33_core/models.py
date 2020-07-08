from django.db import models
from django.contrib.auth.models import User


class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    keyword = models.CharField(max_length=2055)

    searched_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return "{} --> {}".format(self.user.username, self.keyword[:30])

    class Meta:
        ordering = ["-searched_date"]
        verbose_name_plural = 'search histories'
