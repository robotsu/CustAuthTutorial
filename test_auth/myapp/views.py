from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def home(request):
    return HttpResponse('<h1>blog.objcc.com</h1>')

