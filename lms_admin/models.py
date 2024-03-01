from django.db import models
from django.contrib.auth.models import User
from lms_admin.validators import *
from django.core.validators import MinLengthValidator, MaxLengthValidator, RegexValidator, MinValueValidator, MaxValueValidator
from django.core.exceptions import ValidationError

# Create your models here.

class Files(models.Model):
    file_type = models.CharField(max_length=50)
    path = models.FileField(max_length=200)
    model_ob = models.CharField(max_length=100)

class UserInfo(models.Model):
    user_id = models.OneToOneField(User, null=True, on_delete=models.CASCADE)
    mobile = models.CharField(null=True, max_length=50, validators=[RegexValidator(r'^\d{10}$', message="Enter a valid 10-digit mobile number.")])
    gender = models.CharField(max_length=100, choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    city = models.CharField(max_length=50)
    pincode = models.CharField(max_length=20, validators=[RegexValidator(r'^\d{6}$', message="Enter a valid 6-digit pincode.")])
    address = models.CharField(max_length=100)
    user_type = models.CharField(max_length=50)
    qualification = models.CharField(max_length=50, null=True)
    experience = models.CharField(max_length=50, null=True)
    resume = models.ForeignKey(Files, null=True, on_delete=models.CASCADE)
    dob = models.DateField()

    def clean(self):
        if self.user_type not in ['student', 'teacher', 'admin']:
            raise ValidationError("Invalid user type.")

class Course(models.Model):
    name = models.CharField(max_length=250, null=False, validators=[MinLengthValidator(1)])
    tutor = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=10, decimal_places=2, validators=[MinValueValidator(0)])
    image = models.ImageField(upload_to='courses/', null=True)
    description = models.TextField(validators=[MinLengthValidator(100)])
    status = models.IntegerField(default=1)

    def clean(self):
        if not self.image:
            raise ValidationError("Image is required.")

        if len(self.description) < 10:
            raise ValidationError("Description must be at least 10 characters long.")

class Category(models.Model):
    name = models.CharField(max_length=50, validators=[MinLengthValidator(1)])
    image = models.ImageField(upload_to='category/', null=True)
    status = models.IntegerField(default=1)

    def clean(self):
        if not self.image:
            raise ValidationError("Image is required.")

class SubCategory(models.Model):
    name = models.CharField(max_length=100, validators=[MinLengthValidator(1)])
    image = models.ImageField(upload_to='subcategory/', null=True)
    status = models.IntegerField(default=1)
    category = models.ForeignKey(Category, null=False, on_delete=models.DO_NOTHING)

    def clean(self):
        if not self.image:
            raise ValidationError("Image is required.")

class WebsiteData(models.Model):
    section = models.CharField(max_length=100, validators=[MinLengthValidator(1)])
    description = models.TextField(validators=[MinLengthValidator(1)])
    image = models.ImageField(upload_to='pages/', null=True)
    status = models.IntegerField(default=1)

    def clean(self):
        if not self.image:
            raise ValidationError("Image is required.")

class Feedbacks(models.Model):
    stars = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    feedback = models.TextField(validators=[MinLengthValidator(1)])
    name = models.CharField(max_length=100, validators=[MinLengthValidator(1)])
    user = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)

    def clean(self):
        if self.stars < 1 or self.stars > 5:
            raise ValidationError("Stars must be between 1 and 5.")

class Settings(models.Model):
    key = models.CharField(max_length=250, validators=[MinLengthValidator(1)])
    data = models.TextField(validators=[MinLengthValidator(1)])

class Blogs(models.Model):
    title = models.CharField(max_length=255, validators=[MinLengthValidator(1)])
    description = models.TextField(validators=[MinLengthValidator(1)])
    created_by = models.ForeignKey(User, null=True, on_delete=models.DO_NOTHING)
    like = models.IntegerField(default=0)
    status = models.IntegerField(default=1)
    image = models.ImageField(upload_to='blogs/', null=True)

    def clean(self):
        if self.like < 0:
            raise ValidationError("Like count cannot be negative.")

class Queries(models.Model):
    name = models.CharField(max_length=100, validators=[MinLengthValidator(1)])
    email = models.EmailField()
    mobile = models.CharField(max_length=200, validators=[MinLengthValidator(1)])
    message = models.TextField(validators=[MinLengthValidator(1)])

class Assesments(models.Model):
    pass

class Questions(models.Model):
    pass

class Cart(models.Model):
    pass

class Orders(models.Model):
    pass