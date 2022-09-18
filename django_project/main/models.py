import datetime

from django.db import models

# Create your models here.
class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    age = models.IntegerField(default=18)

class Quiz(models.Model):
    title = models.CharField(max_length=100, default = "Quiz 01")
    quizOrder = models.IntegerField(default = 10)
    duration = models.IntegerField()
    is_open = models.BooleanField(default = True)

class Course(models.Model):
    course_name = models.CharField(max_length=100)
    course_num = models.IntegerField()
    is_undergrad = models.BooleanField()
    course_prereq = models.CharField(max_length=200)
    course_difficulty = models.IntegerField(default = 2)

class Question(models.Model):
    text = models.TextField()
    points = models.IntegerField(default = 10)
    correct_answer = models.CharField(max_length=100)
    incorrect_answer = models.CharField(max_length = 100)
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE)

class Book(models.Model):
    book_title = models.CharField(max_length=200)
    genre = models.CharField(max_length=200)
    publish_date = models.DateField(default = datetime.datetime.now())
    numofpages = models.IntegerField(default = 200)
    additional_info = models.JSONField(default = {})

class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)
    books = models.ManyToManyField(Book, related_name="authors")


#addressOfIndex/byte = address + (index * sizeOfElement)