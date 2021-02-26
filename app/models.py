# Application de sondage
import datetime
from django.utils import timezone
from django.db import models


class Question(models.Model):
    question_text = models.CharField(max_length=200)  # questions_text its takes a character field that why i'm
    # passing the question_text as string
    pub_date = models.DateField('date published')  # publication date takes in date time field and that why i'm

    # passing in the timezone.now()object !
    # def was_published_recently(self):
    # return  self.pub_date >= (timezone.now() - datetime.timedelta(days=1))

    def __str__(self):
        return self.question_text


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)



    def __str__(self):
        return self.choice_text
    #Commande utilisé dans le terminal
    # Question.objects.all()
    # Question.objects.filter(id=1) pour filter  l'objet
# Question.objects.filter(question_text__contains='Je cherche une alternance ')
# q = Question.objects.get(pk=1) Meaning -->Get me the object where the primary key is 1 and save it as q
#q.was_published_recently()

#q.choice_set.all()

#Question objects get access to Choice objects. !!!!
#q.choice_set.all()
# <QuerySet [<Choice: Not much>, <Choice: Just hacking again >, <Choice: The sky>, <Choice: coding is art >, <Choice: Just hacking again>]>

#q.choice_set.count()
#5
              # important !"
# The API automatically follows relationships as far as you need.
# Use double underscores to separate relationships.
# This works as many levels deep as you want; there's no limit.
# Find all Choices for any question whose pub_date is in this year
# (reusing the 'current_year' variable we created above).
#pour supprimer
# c = q.choice_set.filter(choice_text__startswith='Just hacking')
#c.delete()
#Choice.objects.filter(question__pub_date__year=current_year)
#<QuerySet [<Choice: Not much>, <Choice: The sky>, <Choice:  coding is art>]>
##q.choice_set.count()
#3


