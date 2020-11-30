from django.db import models
import re
from datetime import date

class UserManager(models.Manager):
    def basic_validator(self, postData):
        errors={}
        if len(postData['first_name'])<2:
            errors['first_name']="First name should be at least 2 characters"
        if len(postData['last_name'])<2:
            errors['last_name']="Last name should be at least 2 characters"
        EMAIL_REGEX=re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if not EMAIL_REGEX.match(postData['email']):
            errors['email']="Invalid email address!"
        else:
            repeatEmail = User.objects.filter(email = postData['email'])
            if len(repeatEmail) > 0:
                errors['emailTaken'] = 'This email is already taken.'
        if postData['password']!=postData['confirm_pw']:
            errors['password']="Passwords do not match"
        if len(postData['password'])<8:
            errors['password']="Password should be at least 8 characters"
        return errors
    def basic_validator2(self, postData):
        errors={}
        if len(postData['title'])<3:
            errors['title']="Title should be at least 3 characters"
        if len(postData['desc'])<3:
            errors['desc']="Description should be at least 3 characters"
        if len(postData['location'])<3:
            errors['location']="Location should be at least 3 characters"
        return errors
        


class User(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    password=models.CharField(max_length=50)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()
    #jobs is a list of all of the jobs one user has

class Job(models.Model):
    posted_by=models.ForeignKey(User, related_name='posted_by', on_delete=models.CASCADE)
    title=models.CharField(max_length=50)
    desc=models.TextField()
    location=models.CharField(max_length=255)
    category=models.CharField(max_length=255)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    objects=UserManager()

class UserJob(models.Model):
    user=models.ForeignKey(User, related_name="job", on_delete=models.CASCADE)
    job=models.ForeignKey(Job, related_name='user', on_delete=models.CASCADE)

