from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views import generic
from .forms import ContactForm
from django.contrib import messages

class BaseTemplateView(generic.TemplateView):
    template_name = 'portfolio_app/index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = ContactForm()  # Añadir el formulario al contexto aquí
        return context

class IndexView(BaseTemplateView):
    def get(self, request, *args, **kwargs):
        context = self.get_context_data()
        return self.render_to_response(context)  # Pasar el contexto que contiene el formulario

    def post(self, request, *args, **kwargs):
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you. We will be in touch soon.')
            return redirect('index')
        else:
            messages.error(request, 'Something went wrong. Please try again.')
            context = self.get_context_data()
            return self.render_to_response(context)  # Pasar el contexto que contiene el formulario
