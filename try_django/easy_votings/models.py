from django.db import models
from django.urls import reverse


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text

class Task(models.Model):
    name = models.CharField('имя', max_length=10)
    surname = models.CharField('фамилия', max_length=15)
    task = models.TextField('описание')


    def __str__(self):
        return self.name
    def get_abcolute_url(self):
        return reverse('post',kwargs={'post_id':self.pk})
    class Meta:
        verbose_name = 'курьер'
        verbose_name_plural = 'курьеры'