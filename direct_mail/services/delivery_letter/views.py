
from django.views.generic import TemplateView, FormView
from .models import DeliveryType

from .forms import LetterForm, LetterOnlyDeliveryForm


class TypeListView(TemplateView):
    template_name = "delivery_letter/type_list.html"

    def get_context_data(self, **kwargs):
        kwargs['delivery_type_list'] = DeliveryType.objects.all()
        return super().get_context_data(**kwargs)


class LetterBaseFormView(FormView):
    template_name = 'delivery_letter/delivery.html'
    success_url = "/"

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)


class LetterFormView(LetterBaseFormView):
    form_class = LetterForm

class LetterOnlyDeliveryFormView(LetterBaseFormView):
    form_class = LetterOnlyDeliveryForm




