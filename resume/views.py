from django.shortcuts import render
from django.views import generic

from .forms import ResumeForm
from .models import Resume


class ResumeCreateView(generic.CreateView):
    model = Resume
    template_name = 'resume/resume_create.html'
    form_class = ResumeForm
    success_url = 'success'


def success_create(request):
    return render(request, 'resume/resume_success.html')