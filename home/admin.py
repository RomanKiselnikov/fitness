from django.contrib import admin

from home.models import AdviseFree


@admin.register(AdviseFree)
class AdviseFree(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'type_product', 'data', 'state',)
    list_editable = ('state',)
    readonly_fields = ('name', 'phone', 'data', 'type_product', 'email',)
    list_filter = ('state', 'type_product',)

    def has_add_permission(self, request):
        return False
