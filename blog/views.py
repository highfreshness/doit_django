from django.shortcuts import render
from .models import Post
# Create your views here.
def index(request):
    # 필요한 코드 넣기
    posts = Post.objects.all().order_by('-pk')
    # render 요소 3가지 (request, html파일(템플릿 파일), {key:value} )
    return render(request, 'blog/index.html', {'posts':posts,})

def single_post_page(request, pk):
    post = Post.objects.get(pk=pk)
    return render(request, 'blog/single_post_page.html', {'post':post})