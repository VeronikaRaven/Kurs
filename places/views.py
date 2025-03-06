from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Place, Review
from .forms import RegistrationForm, ReviewForm
from django.contrib import messages
from django.contrib.auth import login, authenticate

def places(request):
    all_places = Place.objects.all()
    return render(request, 'places/places.html', {'places': all_places})

def place_detail(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    reviews = place.reviews.all()
    review_form = ReviewForm()
    
    return render(request, 'places/place_detail.html', {
        'place': place,
        'reviews': reviews,
        'review_form': review_form
    })

@login_required
def add_review(request, place_id):
    place = get_object_or_404(Place, pk=place_id)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.place = place
            review.user = request.user
            review.save()
            messages.success(request, 'Ваш отзыв успешно добавлен!')
            return redirect('place_detail', place_id=place_id)
    
    return redirect('place_detail', place_id=place_id)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Аккаунт {username} успешно создан!')
            return redirect('places')
    else:
        form = RegistrationForm()
    return render(request, 'places/register.html', {'form': form})
