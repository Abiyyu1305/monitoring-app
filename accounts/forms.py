from django import forms


class RegisterForm(forms.Form):

    nama_lengkap = forms.CharField(
        max_length=100
    )

    email = forms.EmailField()

    no_hp = forms.CharField(
        max_length=20
    )

    divisi = forms.CharField(
        max_length=50
    )

    username = forms.CharField(
        max_length=50
    )

    password = forms.CharField(
        widget=forms.PasswordInput
    )

    confirm_password = forms.CharField(
        widget=forms.PasswordInput
    )
