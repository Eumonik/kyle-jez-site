from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.detail import SingleObjectMixin
from django.core.mail import EmailMessage
from django.shortcuts import redirect
from django.template import Context
from django.template.loader import get_template
from django.contrib import messages

from home.models import Post, Category, Tag
from home.forms import SearchForm, ContactForm

class HomeView(ListView):
    template_name = 'home/base.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Post.objects.order_by('-posted')[:3]

def contact(request):
    form_class = ContactForm
    form = form_class(data=request.POST)

    if request.method == 'POST':

        if form.is_valid():
            contact_name = request.POST.get(
                'contact_name'
            , '')
            contact_email = request.POST.get(
                'contact_email'
            , '')
            contact_message = request.POST.get('contact_message', '')

            messages.success(request, 'All is well with the cosmos. Thank you for your words.')

            # Email the profile with the
            # contact information
            template = get_template('home/contact_template.txt')
            context = Context({
                'contact_name': contact_name,
                'contact_email': contact_email,
                'contact_message': contact_message,
            })
            content = template.render(context)

            email = EmailMessage(
                "New contact form submission",
                content,
                "https://www.kylejezwinski.com" +'',
                ['kylejezwinski@gmail.com'],
                headers = {'Reply-To': contact_email }
            )
            email.send()
            return redirect('contact')

        else:

            messages.error(request, 'Message exterminated. Try a different syntax.')

    return render(request, 'home/contact.html', {
        'form': form_class,
    })


class PostListView(ListView):
    template_name = 'home/posts.html'
    context_object_name = 'posts'
    queryset = Post.objects.order_by('-posted')[:25]

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        context['posts'] = self.queryset
        context['categories'] = Category.objects.all()
        return context

class PostDetailView(DetailView):
    template_name = 'home/post.html'
    model = Post

class CategoriesListView(ListView):
    template_name = 'home/categories.html'
    context_object_name = 'categories'

    def get_queryset(self):
        return Category.objects.all()

class CategorysListView(ListView):
    template_name = 'home/category.html'
    context_object_name = 'posts'

    def get_queryset(self):
        self.category = get_object_or_404(Category, title=self.args[0])
        return Post.objects.filter(category=self.category)

    def get_context_data(self, **kwargs):
        context = super(CategorysListView, self).get_context_data(**kwargs)
        context['category'] = self.category
        return context

class TagListView(ListView):
    template_name = 'home/tags.html'
    context_object_name = 'tags'
    model = Tag


class TagsListView(ListView):
    template_name = 'home/tag.html'
    context_object_name = 'posts'

    def get_queryset(self):
        self.tag = get_object_or_404(Tag, title=self.args[0])
        return Post.objects.filter(tags=self.tag)

    def get_context_data(self, **kwargs):
        context = super(TagsListView, self).get_context_data(**kwargs)
        context['tag'] = self.tag
        return context

def search(request):
    messages.error(request, 'Message exterminated. Try a different syntax.')
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            return HttpResponseRedirect('search/')


    return render(request, 'home/search.html', {'form':form})







'''

def tag_view(request, tag_slug=None):
    object_list = Post.objects.all()
    tag = None

    if tag_slug:
        tag = get_object_or_404(Tag, slug=tag_slug)
        object_list = object_list.filter(tags__in=[tag])
    return render(request, 'home/tag.html', {'tag':tag})

'''




'''
class CategoryPostView(SingleObjectMixin, ListView):
    template_name = 'home/category.html'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object(queryset=Post.objects.all())
        return super(CategoryPostView, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CategoryPostView, self).get_context_data(**kwargs)
        context['post'] = self.object
        return context

    def get_queryset(self):
        return self.object.category

class CategoryPostView(DetailView):
    template_name = 'home/category.html'
    context_object_name = 'category'
    queryset = Category.objects.all()

    def get_context_data(self, **kwargs):
        context = super(CategoryPostView, self).get_context_data(**kwargs)
        context['category'] = self.queryset
        context['posts'] = Post.objects.all()
        return context



class ArchiveIndexView(ArchiveIndexView):
    queryset = Post.objects.all()
    date_list = "posted"
    allow_future = False

class ArchiveDetailView(DetailView):
    template_name = 'home/archive.html'
    context_object_name = 'archive'

    def get_queryset(self):
        return Archive.objects.all()
'''
