from django.db import models


# Create your models here.
# Object relational mapping (ORM) module is a tool that allows you to create, read,
# update, and delete data from a database using an object-oriented paradigm.
class Customers(models.Model):
    Id = models.AutoField(primary_key=True)
    FirstName = models.CharField(max_length=50)
    LastName = models.CharField(max_length=50)
    Address = models.CharField(max_length=50)
    PhoneRes = models.IntegerField()
    EnrollDate = models.DateField()
    IsActive = models.BooleanField()
    CreatedBy = models.CharField(max_length=50)
    CreatedOn = models.DateTimeField(auto_now_add=True)
    UpdatedBy = models.CharField(max_length=50)
    UpdatedOn = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    # __str__  method is defined to return the users name when we call or print the objet
    def __str__(self):
        return self.FirstName

    class Meta:  # to determine the app label for a model. The app label is used to identify which app a model belongs to, and is usually specified in the Meta class of the model.
        db_table = 'Customers'

# class Post(models.Model):
#     title = models.CharField(max_length=200)
#     content = models.TextField()
#     objects = models.Manager()
#     created_at = models.DateTimeField(auto_now_add=True)
