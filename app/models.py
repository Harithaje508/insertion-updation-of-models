from django.db import models

# Create your models here.
class Topic(models.Model):
    topic_name=models.CharField(max_length=100,primary_key=True)
    def __str__(self):
        return self.topic_name

class Webpage(models.Model):
    topic_name=models.ForeignKey(Topic,on_delete=models.CASCADE)
    name=models.CharField(max_length=100)
    url=models.URLField()
    email=models.EmailField(default='haritha.errolla@gmail.com')
    def __str__(self):
        return self.name
    
class Accessrecord(models.Model):
    name=models.ForeignKey(Webpage,on_delete=models.CASCADE)
    date=models.DateField()
    autor=models.CharField(max_length=100)
    def __str__(self):
        return self.name
    
class capital(models.Model):
    cname=models.CharField(max_length=100)
    def __str__(self):
        return self.cname
    
class country(models.Model):
    country_name=models.CharField(max_length=100)
    cname=models.ForeignKey(capital,on_delete=models.CASCADE)
    def __str__(self):
        return self.country_name

