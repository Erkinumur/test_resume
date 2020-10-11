from django.forms import ModelForm, forms

from .models import Resume


class ResumeForm(ModelForm):
    class Meta:
        model = Resume
        fields = '__all__'
        help_texts = {
            'number': 'Введите номер в формате 996ХХХХХХХХХ'
        }

    def clean_number(self):
        number = self.cleaned_data.get('number')
        if len(str(number)) != 12 or not str(number).startswith('996'):
            raise forms.ValidationError('Неверный формат номера.')
        return number
