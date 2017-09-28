# Create your models here.
from django.db import models


class Account(models.Model):
    user_id = models.CharField(max_length=200)
    user_name = models.CharField(max_length=200)

    def __str__(self):
        return self.user_name


class Word(models.Model):
    word_id = models.CharField(max_length=200)
    word_name = models.CharField(max_length=200)
    word_phonetic = models.CharField(max_length=200)
    word_text = models.CharField(max_length=1000)

    def __str__(self):
        return self.word_name
