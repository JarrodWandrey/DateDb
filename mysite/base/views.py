from django.shortcuts import render,redirect
from base.models import Date
from base.forms import DateForm

# Create your views here.
def home(request):
    latest_dates = Date.objects.all()
    context = {
        'latest_dates': latest_dates,
    }
    return render(request, 'home.html', context)

def create_date(request):
    if request.method == 'POST':
        form = DateForm(request.POST)
        if form.is_valid():
            form.save()  # Save the new Date instance to the database
            return redirect('home')  # Redirect to a success page or another page after form submission
    else:
        form = DateForm()

    return render(request, 'create.html', {'form': form})