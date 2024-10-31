from django.shortcuts import render

# Create your views here.
def index(request):
    try:
        uid = request.GET('user_id')
        upass = request.GET('user_pass')
    except:
        uid = None
        
    if uid != None and upass == '12345':
        verified = True
    else:
        verified = False
    return render(request, 'index.html', locals())