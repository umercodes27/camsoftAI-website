from django.shortcuts import render
from blog.models import Post
from django.core.paginator import Paginator

# Create your views here.
def blogHome(request):
    # Get all posts
    allPosts = Post.objects.all()

    # Set up pagination with 4 posts per page (adjust the number as needed)
    paginator = Paginator(allPosts, 4)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    # Pass the page object to the template
    context = {'page_obj': page_obj}
    return render(request, "blog/blogHome.html", context)

def blogPost(request, slug):
    post = Post.objects.filter(slug=slug).first()
    context = {'post': post}
    return render(request, 'blog/blogPost.html', context)
