from django.shortcuts import render,HttpResponse
from .models import Posts ,like_post    
# Create your views here.

def index(request):
    post=Posts.objects.all()
    likecount=like_post.objects.all().count()
    context={'post':post,'likecount':likecount}
    return render(request,'post/index.html',context)

def likePost(request):
    if request.method=="GET":
        post_id=request.GET['post_id']
        likepo=Posts.objects.get(pk=post_id)
        obj=like_post(post=likepo)
        obj.save()
        return HttpResponse("Success!")
    else:
       return HttpResponse("Request is not get")


        