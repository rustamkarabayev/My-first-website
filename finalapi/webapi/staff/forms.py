from django import forms

from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['name', 'email', 'phone', 'message']

        widgets = {

            'name': forms.TextInput(attrs={'placeholder': "Ваше имя:", 'class': 'form-control'}),
            'email': forms.TextInput(attrs={'placeholder': "Ваш e-mail:", 'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'placeholder': "Ваш номер телефона:", 'class': 'form-control'}),
            'message': forms.Textarea(attrs={'placeholder': "Ваш отзыв:", 'class': 'form-control mb-5'}),
        }
