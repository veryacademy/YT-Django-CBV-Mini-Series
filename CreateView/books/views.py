from django.views.generic.base import TemplateView
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from django.views.generic.edit import FormView, CreateView
from books.models import Books
from . forms import AddForm
from django.db.models import F
from django.utils import timezone


""" 
class AddBookView(FormView):

    template_name = 'add.html'
    form_class = AddForm
    success_url = '/books/'

    def form_valid(self, form):
        form.save()
        return super().form_valid(form) 
"""


class AddBookView(CreateView):
    model = Books
    form_class = AddForm
    template_name = 'add.html'
    success_url = '/books/'


class IndexView(ListView):

    model = Books
    template_name = "home.html"
    context_object_name = 'books'
    paginate_by = 4
    #queryset = Books.objects.all()[:2]

    # def get_queryset(self):
    # return Books.objects.all()[:3]


class GenreView(ListView):
    model = Books
    template_name = 'home.html'
    context_object_name = 'books'
    paginate_by = 2  # Pagination over-write

    def get_queryset(self, *args, **kwargs):
        return Books.objects.filter(genre__icontains=self.kwargs.get('genre'))


class BookDetailView(DetailView):

    model = Books
    template_name = 'book-detail.html'
    context_object_name = 'book'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        post = Books.objects.filter(slug=self.kwargs.get('slug'))
        post.update(count=F('count') + 1)

        context['time'] = timezone.now()

        return context
