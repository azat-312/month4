from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name


class Tag (models.Model):
    name = models.CharField(max_length=25)

    def __str__(self):
        return self.name
    

class Post(models.Model):
    image = models.ImageField(null=True,blank=True)
    title = models.CharField(max_length=200)
    content = models.CharField(max_length=500)
    rate = models.IntegerField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    category = models.ForeignKey(Category,null=True,
            on_delete=models.PROTECT)
    tags = models.ManyToManyField(Tag , null=True,blank=True )

    def __str__(self):
        return f"{self.title} - {self.content}"