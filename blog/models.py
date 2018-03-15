from django.db import models
from django.utils import timezone
from django.urls import reverse
# Create your models here.

class BlogPost(models.Model):
    author = models.ForeignKey('auth.User')
    title = models.CharField(max_length=50)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date =models.DateTimeField(blank=True, null=True)

    def get_absolute_url(self):
        return reverse('blog:blogdetail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

    def publish(self):
        self.published_date = timezone.now()
        self.save()


class GamePlay(models.Model):
    LEFT = 'LT'
    RIGHT = 'RT'
    LEFTRIGHT_CHOICES = (
        (LEFT, '왼쪽'),
        (RIGHT, '오른쪽')
    )
    leftright = models.CharField(max_length=2, choices=LEFTRIGHT_CHOICES)
    usr = models.ForeignKey('auth.User')
    created_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.leftright