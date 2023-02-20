from django.http import HttpResponse


def index(request):
    return HttpResponse('&#128571;')


def second_page(request):
    return HttpResponse('А это вторая страница!')
