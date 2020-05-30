from .models import Post
from django.shortcuts import render
from django.views import generic

def PostList(request):
       key=Post.objects.all()
       return render(request,'index.html',{'data':key})
class PostDetail(generic.DetailView):
       model = Post
       template_name = 'detail.html'

class PostCreateView(generic.CreateView):
       model = Post
       fields = ['title','author','content']
       template_name='post_form.html'

class PostUpdateView(generic.UpdateView):
      model = Post
      fields = ['title' ,'content']
      template_name = 'post_form.html'

class PostDeleteView(generic.DeleteView):
      model=Post
      template_name='post_confirm_delete.html'
      success_url='/'

