from django.db import models


# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=50)
    date_of_birth = models.DateField()
    mobile = models.IntegerField()
    email_id = models.EmailField()
    course_name = models.CharField(max_length=100)
    mark = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class college(models.Model):
    college_name = models.CharField(max_length=250)
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.college_name


class ADMIN(models.Model):
    username = models.CharField(max_length=30)
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.username


class science(models.Model):
    course = models.CharField(max_length=300)
    college = models.CharField(max_length=300)


class commerce(models.Model):
    course = models.CharField(max_length=300)
    college = models.CharField(max_length=300)


class literature(models.Model):
    course = models.CharField(max_length=300)
    college = models.CharField(max_length=300)


class humanities(models.Model):
    course = models.CharField(max_length=300)
    college = models.CharField(max_length=300)


class finearts(models.Model):
    course = models.CharField(max_length=300)
    college = models.CharField(max_length=300)


class journalism(models.Model):
    course = models.CharField(max_length=300)
    college = models.CharField(max_length=300)


class engineering(models.Model):
    course = models.CharField(max_length=300)
    college = models.CharField(max_length=300)


class law(models.Model):
    course = models.CharField(max_length=300)
    college = models.CharField(max_length=300)
