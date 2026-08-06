from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

from .forms import RegisterForm
from .models import Profile


def register_view(request):

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            password = form.cleaned_data['password']
            confirm = form.cleaned_data['confirm_password']

            if password != confirm:

                return render(
                    request,
                    'accounts/register.html',
                    {
                        'form': form,
                        'error': 'Password dan Konfirmasi Password tidak sama'
                    }
                )

            # Cek username sudah ada atau belum
            if User.objects.filter(
                username=form.cleaned_data['username']
            ).exists():

                return render(
                    request,
                    'accounts/register.html',
                    {
                        'form': form,
                        'error': 'Username sudah digunakan'
                    }
                )

            # Cek email sudah ada atau belum
            if User.objects.filter(
                email=form.cleaned_data['email']
            ).exists():

                return render(
                    request,
                    'accounts/register.html',
                    {
                        'form': form,
                        'error': 'Email sudah terdaftar'
                    }
                )

            user = User.objects.create_user(
                username=form.cleaned_data['username'],
                email=form.cleaned_data['email'],
                password=password
            )

            Profile.objects.create(
                user=user,
                nama_lengkap=form.cleaned_data['nama_lengkap'],
                no_hp=form.cleaned_data['no_hp'],
                divisi=form.cleaned_data['divisi']
            )

            messages.success(
                request,
                'Akun berhasil dibuat. Silakan login.'
            )

            return redirect('login')

    else:

        form = RegisterForm()

    return render(
        request,
        'accounts/register.html',
        {
            'form': form
        }
    )


def login_view(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('dashboard')

        else:

            return render(
                request,
                'accounts/login.html',
                {
                    'error': 'Username atau Password salah'
                }
            )

    return render(
        request,
        'accounts/login.html'
    )


def logout_view(request):

    logout(request)

    messages.success(
        request,
        'Berhasil logout.'
    )

    return redirect('login')
