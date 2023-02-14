from django.shortcuts import render, redirect
from django.core.handlers.wsgi import WSGIRequest
from webapp.models import Article

db = []


def add_view(request: WSGIRequest):
    if request.method == "GET":
        return render(request, 'article_create.html')
    print(request.POST)
    article_data = {
        'description': request.POST.get('description'),
        'date': request.POST.get('date'),
        'status': request.POST.get('status'),
    }
    article = Article.objects.create(**article_data)
    return redirect(f'/article/?pk={article.pk}')


def detail_view(request):
    article_pk = request.GET.get('pk')
    article = Article.objects.get(pk=article_pk)
    context = {'article': article}
    return render(request, 'article.html', context=context)



