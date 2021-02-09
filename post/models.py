from django.db import models

# Create your models here.

class Posts(models.Model):
       post_heading=models.CharField(max_length=200, blank=True, null=True)
       post_text = models.TextField(null=True)
       
       def __str__(self):
            return self.post_heading


class like_post(models.Model):
       post=models.ForeignKey(Posts, related_name='posts_child', on_delete=models.CASCADE)    
       
       def __str__(self):
              return self.post.post_heading