from .models import Task
from django.forms import ModelForm, TextInput, Textarea


class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ["name", "task", "phone_num", "mail", "name_car"]
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Введите имя'
            }), "task": Textarea(attrs={
                    'class': 'form-control',
                    'placeholder': 'Введите комментарий'
                }), "phone_num": TextInput(attrs={
                        'class': 'form-control',
                        'placeholder': 'Введите номер телефона'
                    }), "mail": TextInput(attrs={
                            'class': 'form-control',
                            'placeholder': 'Введите электронную почту'
                        }), "name_car": TextInput(attrs={
                                'class': 'form-control',
                                'placeholder': 'Введите название машины'})}