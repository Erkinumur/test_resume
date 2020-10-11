from django import forms

from .models import Resume


class ResumeForm(forms.ModelForm):
    class Meta:
        model = Resume
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(
                attrs={"class": "form-control", "placeholder": 'Имя'}),
            'last_name': forms.TextInput(
                attrs={"class": "form-control", "placeholder": 'Фамилия'}),
            'patronymic': forms.TextInput(
                attrs={"class": "form-control", "placeholder": 'Отчество'}),
            'number': forms.NumberInput(
                attrs={"class": "form-control", "placeholder": 'Номер '
                                                               'телефона'}),
            'email': forms.EmailInput(
                attrs={"class": "form-control", "placeholder": 'Email'}),
            'department': forms.Select(
                attrs={"class": "form-control"}),
            'description': forms.Textarea(
                attrs={"class": "form-control", "placeholder": 'Описание'}),
            'experience': forms.Textarea(
                attrs={"class": "form-control", "placeholder": 'Опыт'}),
        }
        help_texts = {
            'number': 'Введите номер в формате 996ХХХХХХХХХ'
        }

    def clean_number(self):
        number = self.cleaned_data.get('number')
        if len(str(number)) != 12 or not str(number).startswith('996'):
            raise forms.ValidationError('Неверный формат номера.')
        return number
