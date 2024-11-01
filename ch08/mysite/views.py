from django.shortcuts import render
from mysite import models

# Create your views here.
def index(request):
    posts = models.Post.objects.filter(enabled=True).order_by('-pub_time')[:30]
    moods = models.Mood.objects.all()
    try:
        user_id = request.GET('user_id')
        user_pass = request.GET('user_pass')
        user_post = request.GET('user_post')
        user_mood = request.GET('user_mood')
    except:
        user_id = None
        message = 'If you want to paste message, all fiels are required.'

    if user_id != None:
        mood = models.Mood.objects.get(status=user_mood)
        post = models.Post(mood=mood, nickname=user_id, del_pass=user_pass, message=user_post)
        post.save()
        message = 'Mood is saved, please waiting for post and remember you edit password[{}]'.format(user_pass)
        
    return render(request, 'index.html', locals())