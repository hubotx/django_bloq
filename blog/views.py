from django.shortcuts import get_object_or_404, render
from .models import Post


# Create your views here.
def post_list(request):
    posts = Post.published.all()
    return render(request, 'blog/post/list.html', {'posts': posts})


def post_detail(request, year, month, day, slug):
    post = get_object_or_404(Post,
                             published__year=year,
                             published__month=month,
                             published__day=day,
                             published__slug=slug)
    return render(request, 'blog/post/detail.html', {'post': post})
