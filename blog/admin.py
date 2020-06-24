from django.contrib import admin

# importer son model 

from .models import Post

#j'enregistre mon model :

admin.site.register(Post)
