from django.shortcuts import render, get_object_or_404
from .models import Post, Category, Comment
from django.views.generic import DetailView, UpdateView, DeleteView, CreateView
from .forms import PostForm, CommentForm
from django.urls import reverse_lazy, reverse
from django.http import HttpResponseRedirect
from django.db.models import Q
# Create your views here.


def home(request):
    search_query = request.GET.get('search-area')
    if search_query:
        posts = Post.objects.filter(title__icontains=search_query) #title__icontains=search_query,category__icontains=search_query


    else:
        posts = Post.objects.order_by('-id')


    return render(request, 'main/home.html', {'posts': posts})


def likeview(request, pk):
    post = get_object_or_404(Post, id=request.POST.get('post_id'))
    liked = False
    if post.like.filter(id=request.user.id).exists():
        post.like.remove(request.user)
        liked = False
    else:
        post.like.add(request.user)
        liked = True
    return HttpResponseRedirect(reverse('full-post', args=[str(pk)]))


def categoryview(request, cats):
    category_posts = Post.objects.filter(category=cats.replace('-', ' ')).order_by('-id')
    return render(request, 'main/categories.html',  {'cats': cats.title().replace(' ', ''), 'category_posts':category_posts})


class PostDetailView(DetailView):
    model = Post
    template_name = 'main/post_details.html'

    def get_context_data(self, *args, **kwargs):
        context = super(PostDetailView, self).get_context_data(*args, **kwargs)

        stuff = get_object_or_404(Post, id=self.kwargs['pk'])
        total_likes = stuff.total_likes()

        liked = False
        if stuff.like.filter(id=self.request.user.id).exists():
            liked = True

        context["total_likes"] = total_likes
        context["liked"] = liked
        return context

class CreatePostView(CreateView):
    model = Post
    form_class = PostForm
    template_name = 'main/create_post.html'
    #fields = '__all__'
    #fields = ('title', 'body')


class AddCommentView(CreateView):
    model = Comment
    form_class = CommentForm
    template_name = 'main/add_comment.html'

    def form_valid(self, form):
        form.instance.post_id = self.kwargs['pk']
        form.instance.name = self.request.user.username
        return super().form_valid(form)

    def get_success_url(self):
        return reverse_lazy('full-post', kwargs={'pk': self.kwargs['pk']})


class CreateCategoryView(CreateView):
    model = Category
    #form_class = PostForm
    template_name = 'main/create_category.html'
    fields = '__all__'


class UpdatePostView(UpdateView):
    model = Post
    template_name = 'main/update_post.html'
    fields = ['title', 'body']


class DeletePostView(DeleteView):
    model = Post
    template_name = 'main/delete_post.html'
    success_url = reverse_lazy('home')

