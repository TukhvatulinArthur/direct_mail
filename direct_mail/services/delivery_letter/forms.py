from django import forms

from .models import Letter


class LetterForm(forms.ModelForm):
    class Meta:
        model = Letter
        exclude = ['total_price']

    def get_total_price(self):
        """
         :return: Возвращает общую сумму заказа
        """
        total_number = 0
        for audience in self.cleaned_data['audience']:
            total_number += audience.number

            return self.instance.delivery_type.price * total_number

    def save(self, commit=True):
        self.instance.total_price = self.get_total_price()
        return super().save(commit=True)

