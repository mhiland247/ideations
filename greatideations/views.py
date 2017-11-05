import socket
import json
import operator
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect, render_to_response
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from .models import ContactEntry
from django.views.decorators.csrf import csrf_protect, requires_csrf_token
from django.contrib.auth.forms import UserCreationForm
from django.core.mail import send_mail
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib.auth import logout


# Create your views here.

def landing_page(request):
    return render(request, 'greatideations/index.html')

@requires_csrf_token
def contact_post(request):
    if request.method == 'POST':
        post_text = request.POST.get('the_post')
        response_data = {}

        post = ContactEntry(message=post_text, created_date=timezone.now())
        post.save()

        response_data['result'] = 'Message was submited, thank you!'
        response_data['message'] = post.message
        response_data['created_date'] = post.created_date.strftime('%B %d, %Y')

        return HttpResponse(
            json.dumps(response_data),
            content_type="application/json"
        )
    else:
        return HttpResponse(
            json.dumps({"nothing to see": "this isn't happening"}),
            content_type="application/json"
        )

'''def main_page(request):
    return render(request, 'registration/main.html')

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            new_user = form.save()
            return HttpResponseRedirect('/main/')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})'''

