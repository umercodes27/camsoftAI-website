from django.shortcuts import render, HttpResponse, redirect
from home.models import Contact
from django.contrib import messages 
from blog.models import Post
import logging

def home(request): 
    return render(request, "home/home.html")

def contact(request):
    if request.method=="POST":
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        content =request.POST['content']
        if len(name)<2 or len(email)<3 or len(phone)<10 or len(content)<4:
            messages.error(request, "Please fill the form correctly")
        else:
            contact=Contact(name=name, email=email, phone=phone, content=content)
            contact.save()
            messages.success(request, "Your message has been successfully sent")
    return render(request, "home/contact.html")


logger = logging.getLogger(__name__)

def search(request):
    query=request.GET['query']
    if len(query)>78:
        allPosts=Post.objects.none()
    else:
        allPostsTitle= Post.objects.filter(title__icontains=query)
        allPostsAuthor= Post.objects.filter(author__icontains=query)
        allPostsContent =Post.objects.filter(content__icontains=query)
        allPosts=  allPostsTitle.union(allPostsContent, allPostsAuthor)
        logger.info(f"Query: {query}, Results: {allPosts}") 
    if allPosts.count()==0:
        messages.warning(request, "No search results found. Please refine your query.")
    params={'allPosts': allPosts, 'query': query}
    return render(request, 'home/search.html', params)


def about(request): 
    return render(request, "home/about.html")

def service(request): 
    return render(request, "home/service.html")

def features(request): 
    return render(request, "home/features.html")

def price(request): 
    return render(request, "home/price.html")

def quote(request): 
    return render(request, "home/quote.html")

def team(request): 
    return render(request, "home/team.html")

def testimonial(request): 
    return render(request, "home/testimonial.html")
