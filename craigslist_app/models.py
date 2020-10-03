from django.db import models


class Search(models.Model):
    SearchField = models.CharField(max_length=200)
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.SearchField
        
    class Meta:
        verbose_name_plural = "Searches"