from django.shortcuts import render

# Create your views here.
def load_index_page(request):
    return render(request,'blog_main.html',{})