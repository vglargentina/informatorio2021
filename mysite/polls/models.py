import datetime

from django.db import models
from django.utils import timezone


class Noticia(models.Model):

	
	titulo = models.CharField(max_length=200)
	contenido = models.TextField()
	fecha_creacion = models.DateTimeField(default=timezone.now)
	fecha_publicacion = models.DateTimeField(blank=True, null=True)

	def publicar(self):
		self.fecha_publicacion= timezone.now()
		self.save()

	def __str__(self):
		return self.titulo

	class Meta:
		verbose_name =("Noticia")
		verbose_name_plural =("Noticia")



class Question(models.Model):
    question_text = models.CharField(max_length=200)  
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text