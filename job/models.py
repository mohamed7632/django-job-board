from django.db import models
JOB_TYPE=(
    ('full time','full time'),
    ('part time','part time')
)
# Create your models here.
class Job(models.Model):
      title=models.CharField(max_length=100)
      #location
      job_type=models.CharField(max_length=15,choices=JOB_TYPE)
      descreption=models.TextField(max_length=1000)
      published_at=models.DateTimeField(auto_now=True)
      vacancy=models.IntegerField(default=1)
      salary=models.IntegerField(default=0)
      experience=models.IntegerField(default=1)

      def __str__(self):
          return self.title
   