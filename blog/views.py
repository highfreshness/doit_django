from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post
# Create your views here.

# blog list up
# def index(request):
#     # 필요한 코드 넣기
#     posts = Post.objects.all().order_by('-pk')
#     # render 요소 3가지 (request, html파일(템플릿 파일), {key:value} )
#     return render(request, 'blog/index.html', {'posts':posts,})

class PostList(ListView):
    model = Post # 클래스명
    ordering = '-pk'
    # template_name = 'blog/index.html' # 템플릿
    

# 하나의 post 상세 페이지
# def single_post_page(request, pk):
#     post = Post.objects.get(pk=pk)
#     return render(request, 'blog/single_post_page.html', {'post':post})

class PostDetail(DetailView):
    model = Post