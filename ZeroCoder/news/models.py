from django.db import models
from django.contrib.auth.models import User  # импорт модели пользователя

class News_post(models.Model):
    
    title = models.CharField('Название новости', max_length=50)
    
    short_description = models.CharField('Краткое описание новости', max_length=200)
   
    text = models.TextField('Новость')
    pub_date = models.DateTimeField('Дата публикации')
    
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор', null=True)  # Разрешить NULL
	# или
	# author = models.ForeignKey(User, on_delete=models.CASCADE, default=1)  # Указать default

    

    def __str__(self):
        return self.title
