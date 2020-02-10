from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponse
from django.views import View
from .models import Student
from .forms import StudentForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
# Create your views here.


class MyView(View):

    def get(self, request):
        students = Student.objects.all()
        return render(request, 'example/home.html', {'students': students})


class MyListView(ListView):
    model = Student
    template_name = 'example/generic.html'
    context_object_name = 'students'


class MyDetailView(DetailView):
    model = Student
    template_name = 'example/student_detail.html'


class MyCreateView(CreateView):
    template_name = 'example/student_create.html'
    form_class = StudentForm
    queryset = Student.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('list-view')


class MyUpdateView(UpdateView):
    template_name = 'example/student_create.html'
    form_class = StudentForm
    queryset = Student.objects.all()

    def form_valid(self, form):
        print(form.cleaned_data)
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('list-view')


class MyDeleteView(DeleteView):
    model = Student
    template_name = 'example/student_delete.html'

    def get_success_url(self):
        return reverse('list-view')
