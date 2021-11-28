from .models import Task, Task
from django.forms import ModelForm, widgets, TextInput,Textarea

class TaskForm(ModelForm):
    class Meta:
        model = Task
        fields = ['title','task']
        widgets = {'title':TextInput(attrs={
            'class':'form-control',
            'placeholder':'Введите название'
        }),
        'task':widgets.Textarea(attrs={
            'class':'form-control',
            'placeholder':'Введите описание'
        })
        
        }