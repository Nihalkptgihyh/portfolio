from django.shortcuts import render
from django.shortcuts import redirect
from .forms import EmailForm
from .models import Email

def save_email(request):
    if request.method == 'POST':
        form = EmailForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = EmailForm()
    return render(request, 'community.html', {'form': form})
def index(request):
    return render(request, 'index.html')
def contact(request):
    return render(request, 'contact.html')
def about(request):
    return render(request, 'about.html')
def qulification(request):
    return render(request, 'qulification.html')
def experince(request):
    return render(request, 'experince.html')
def community(request):
    return render(request,'community.html')