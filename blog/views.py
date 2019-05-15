from django.shortcuts import render
# from django.http import HttpResponse

posts = [
    {
        'author': 'Randy Galeano',
        'title': 'Blog Post 1',
        'content': 'First Post Content',
        'date_posted': 'May 15, 2019'
    },
    {
        'author': 'Jane Doe',
        'title': 'And album by Converge',
        'content': 'Second Post Content',
        'date_posted': 'May 13, 2019'
    }    
]

# Create your views here.
def home(request):
    context = {
        'posts': posts
    }
    return render(request, 'blog/home.html', context)

def about(request):
    return render(request, 'blog/about.html')