from django.db import models

# je fais une classe abstraite pour éviter de dupliquer du code ( time sera utiliser souvent)
class TimesModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta :
        abstract = True


#Création de mon model "Post", qui va gérer/créer les articles dans ma base de données
class Post(TimesModel):

    title = models.CharField(max_length=255)
    body = models.TextField()

    def __str__(self):
         return self.title

