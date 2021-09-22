from django.db import models


# Формы связи
class AdviseFree(models.Model):
    """Форма бесплатной консультации"""
    name = models.CharField(verbose_name='Имя', max_length=200)
    phone = models.CharField(verbose_name='Телефон', max_length=25)
    email = models.EmailField(verbose_name='Почта')
    type_product = models.CharField(verbose_name='Продукт', default='Не выбрал продукт', max_length=200)
    data = models.DateTimeField(verbose_name='Время запроса', auto_now=True)
    state = models.BooleanField(verbose_name='Провели консультацию', default=False)

    def __str__(self):
        return f"Заявка от {self.name}"

    class Meta:
        verbose_name = "Заявка"
        verbose_name_plural = "Заявки"
