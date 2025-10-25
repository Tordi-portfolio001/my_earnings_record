from django.shortcuts import render, redirect, get_object_or_404
from .models import Earning
from .forms import EarningForm
from django.contrib.auth.decorators import login_required


def earnings_list(request):
    records = Earning.objects.all().order_by('-date')
    return render(request, 'earnings_list.html', {'records': records})

def earnings_detail(request, pk):
    record = get_object_or_404(Earning, pk=pk)
    return render(request, 'earnings_detail.html', {'record': record})

@login_required
def add_earning(request):
    if request.method == 'POST':
        form = EarningForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('earnings_list')
    else:
        form = EarningForm()
    return render(request, 'add_earning.html', {'form': form})

from django.contrib.auth import logout
from django.shortcuts import redirect

def logout_user(request):
    logout(request)
    return redirect('earnings_list')