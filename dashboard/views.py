from django.shortcuts import render

from accounts.models import Profile


def dashboard(request):
    profile = None

    if request.user.is_authenticated:
        profile, created = Profile.objects.get_or_create(user=request.user)

    context = {
        'profile': profile,
    }

    return render(
        request,
        'dashboard/index.html',
        context
    )
