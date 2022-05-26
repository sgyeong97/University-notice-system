from django.views.generic import ListView, DetailView, CreateView
from .models import Profile
from .models import Post


class PostListView(ListView):
    model = Post
    template_name = 'notice/list.html'
    context_object_name = 'posts'

    def get_queryset(self):
        user = self.request.user
        try:
            tag_list = user.profile.tag.names()
        except Profile.DoesNotExist:
            tag_list = []
        return Post.objects.filter(tag__name__in=tag_list)


class PostDetailView(DetailView):
    model = Post
    template_name = 'notice/detail.html'
    context_object_name = 'post'


class PostingView(CreateView):
    model = Post
    fields = ['title', 'body', 'file', 'tag']
    template_name = 'notice/post.html'
    success_url = '/notice'

    def form_valid(self, form):
        form.instance.creator = self.request.user
        return super().form_valid(form)

    def form_invalid(self, form):
        return super().form_invalid(form)
