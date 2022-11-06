


from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.db.models import Count

class MyUser(AbstractUser):
    phone=models.CharField(max_length=200)
    profile_pic=models.ImageField(upload_to="profile_pic",null=True)

class Questions(models.Model):
    user=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    discription=models.CharField(max_length=120)
    image=models.ImageField(upload_to="img",null=True,blank=True)
    created_date=models.DateTimeField(auto_now_add=True)
    is_active=models.BooleanField(default=True)

    
    def fetch_answer(self):
        answer=self.answers_set.all().annotate(u_count=Count("up_vote")).order_by("-u_count")
        return answer


    def __str__(self):
        return self.discription

class Answers(models.Model):
    user=models.ForeignKey(MyUser,on_delete=models.CASCADE)
    qustion=models.ForeignKey(Questions,on_delete=models.CASCADE)
    answer=models.CharField(max_length=200)
    created_date=models.DateTimeField(auto_now_add=True)
    up_vote=models.ManyToManyField(MyUser,related_name="upvote")






