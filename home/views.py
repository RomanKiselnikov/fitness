from django.conf import settings
from django.core.mail import send_mail
from django.http import JsonResponse
from django.shortcuts import render
from django.views import View

from home.forms import AdviseFreeForm


class index(View):
    def get(self, request):
        return render(request, "home/index.html", {})


class AdviseFreeView(View):
    """Заявки"""

    def post(self, request):
        response_data = {}
        form = AdviseFreeForm(request.POST)
        if form.is_valid():
            form.save()
            response_data['status'] = True
            response_data['message'] = 'Спасибо'
            send_mail('Обращение', f'Имя: {request.POST["name"]}\n'
                                   f'Телефон: {request.POST["phone"]}\n'
                                   f'Почта: {request.POST["email"]}\n'
                                   f'Продукт: {request.POST["type_product"]}\n', settings.EMAIL_HOST_USER,
                      [
                          'ksenia2807@bk.ru',
                          # 'nail.velichko2016@yandex.ru'
                       ])
        else:
            response_data['status'] = False
            response_data['message'] = 'Ошибка'
            response_data['form'] = form._errors
        return JsonResponse(response_data, safe=False)
