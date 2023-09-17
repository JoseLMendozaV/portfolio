from django.shortcuts import render
from django.http import HttpResponse
from django.views import generic
from . forms import ContactForm
from django.contrib import messages



def index(request):
    return render(request, 'portfolio_app/index.html')



class ContactView(generic.FormView):
	template_name = "portfolio_app/index.html"
	form_class = ContactForm
	success_url = "/"
	
	def form_valid(self, form):
		form.save()
		messages.success(self.request, 'Thank you. We will be in touch soon.')
		return super().form_valid(form)