from django.db import models
from django.core.validators import MinLengthValidator,MaxLengthValidator


# Create your models here.

class Tag(models.Model):
    caption=models.CharField(max_length=20)

    def __str__(self):
     return self.caption    

class Author(models.Model):
    firstname=models.CharField(max_length=100)
    lastname=models.CharField(max_length=100)
    email_address=models.EmailField()
    
    def fullname(self):
        return f"{self.firstname} {self.lastname}"
 
    def __str__(self):
        return self.fullname()    

class Post(models.Model):
    title=models.CharField(max_length=150)
    excerpt=models.CharField(max_length=200)
    image =models.ImageField(upload_to="posts", null=True)
    date=models.DateField(auto_now=True)
    slug=models.SlugField(unique=True,db_index=True)
    content=models.TextField(validators=[MinLengthValidator(10)])
    author=models.ForeignKey(Author,null=True,on_delete=models.SET_NULL,related_name="posts")
    tags=models.ManyToManyField(  Tag)

    
   

