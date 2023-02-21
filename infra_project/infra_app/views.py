from django.http import HttpResponse


def index(request):
    return HttpResponse('Ну, получилось ли??')


def second_page(request):
    return HttpResponse('А это вторая страница!')
