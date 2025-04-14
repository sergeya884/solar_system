from django import forms

class CelestialBodyForm(forms.Form):
    name = forms.CharField(label='Введите имя планеты или спутника', max_length=100, required=True)

    def clean_name(self):
        name = self.cleaned_data.get('name')
        if not name:
            raise forms.ValidationError("Это поле обязательно для заполнения.")
        if not name.isalpha():
            raise forms.ValidationError("Имя должно содержать только буквы.")
        return name

class LeaderboardForm(forms.Form):
    name = forms.CharField(label='Ваше имя', max_length=100, required=True)