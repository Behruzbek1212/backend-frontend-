from django.db import models

class Post(models.Model):
    name = models.CharField("Ism",max_length=255)
    content = models.TextField("malumot")
    tanlov = models.CharField("tanlov",max_length=255)
    date = models.DateTimeField("vaqti",auto_now_add=True)
    rasm = models.CharField("rasm",max_length=255)

    def __str__(self):
        return self.name


class TopPost(models.Model):
    name = models.CharField("Nomi",max_length=255)
    tanlov = models.CharField("Tanlov",max_length=255)
    date = models.DateTimeField("Vaqti",auto_now_add=True)
    rasm = models.CharField("Rasm",max_length=255)

    def __str__(self):
        return self.name
    
class Admin(models.Model):
    name = models.CharField("Ismi",max_length=225)
    content = models.TextField("Malumot")
    # date = models.DateTimeField("Vaqt",auto_now_add=True)
    # img = models.CharField("Rasm",max_length=255)

    def __str__(self):
        return self.name