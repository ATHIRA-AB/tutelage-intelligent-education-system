from django.db import models

# Create your models here.
class pmodel(models.Model):
    
    ccode = models.CharField(max_length=20)
    scode = models.CharField(max_length=20)
    ttid = models.CharField(max_length=10)
    descp = models.CharField(max_length=10)
    path = models.FileField(upload_to='uploads')

    class Meta:
        db_table = "tbl_notes"