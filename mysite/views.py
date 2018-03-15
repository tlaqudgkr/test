from django.views.generic.base import TemplateView
from blog.models import GamePlay
from django.http import JsonResponse

class HomeView(TemplateView):
    template_name = 'home.html'


def myGamePlay(request):
    user = request.user
    myDir = request.GET['dir']
    GamePlay.objects.create(usr=user, leftright=myDir)
    mycount = GamePlay.objects.filter(usr=user, leftright=myDir).count()
    result = {'myDir':myDir, 'mycount':mycount}
    return JsonResponse(result)