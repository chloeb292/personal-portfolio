from django.db import models

class Experience(models.Model):
    title = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.title

# make a model for medium articles that will have a title, description, a picture and a link
class Article(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    # image = models.ImageField(upload_to='images/')
    img_link = models.URLField(max_length=200)
    link = models.URLField(max_length=200)

    def __str__(self):
        return self.title