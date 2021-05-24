from django.db import models
from django.db.models.deletion import CASCADE
JOB_TYPE=(
    ('full time','full time'),
    ('part time','part time')
)
def upload_img(instance,filename):
    imgname,extension=filename.split(".")
    return "jobs/%s.%s"%(instance.id,extension)

# Create your models here.
class Job(models.Model):
      title=models.CharField(max_length=100)
      #location
      job_type=models.CharField(max_length=15,choices=JOB_TYPE)
      descreption=models.TextField(max_length=1000)
      published_at=models.DateTimeField(auto_now=True)
      vacancy=models.IntegerField(default=1)
      image=models.ImageField(upload_to=upload_img)
      salary=models.IntegerField(default=0)
      experience=models.IntegerField(default=1)
      category=models.ForeignKey('Category',on_delete=models.CASCADE)

      def __str__(self):
          return self.title

class Category(models.Model):
    name=models.CharField(max_length=20)
    def __str__(self):
        return self.name