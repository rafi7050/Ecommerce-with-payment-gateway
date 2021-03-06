from django.contrib import admin

from .models import Item, OrderItem, Order, Payment, Coupon, Refund, BillingAddress, UserProfileInfo, ObjectViewed

# Register your models here.


def make_refund_accepted(modeladmin, request, queryset):
    queryset.update(refund_requested=False, refund_granted=True)


make_refund_accepted.short_description = 'Update orders to refund granted'


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user',
                    'ordered',
                    'being_delivered',
                    'received',
                    'refund_requested',
                    'refund_granted',
                    'shipping_address',
                    'billing_address',
                    'payment',
                    'coupon'
                    ]
    list_display_links = [
        'user',
        'shipping_address',
        'billing_address',
        'payment',
        'coupon'
    ]
    list_filter = ['user',
                   'ordered',
                   'being_delivered',
                   'received',
                   'refund_requested',
                   'refund_granted']
    search_fields = [
        'user__username',
        'ref_code'
    ]
    actions = [make_refund_accepted]


class AddressAdmin(admin.ModelAdmin):
    list_display = [
        'user',
        'street_address',
        'apartment_address',
        'country',
        'zip',
        'address_type',
        'default'
    ]
    list_filter = ['default', 'address_type', 'country']
    search_fields = ['user', 'street_address', 'apartment_address', 'zip']


class ItemAdmin(admin.ModelAdmin):
    search_fields = ["title"]

class UserProfileInfoAdmin(admin.ModelAdmin):
    list_display = ('user', 'portfolio_site', 'profile_pic', 'job', 'o_date', 'd_date', 'fn', 'ln', 'ads', 'status')
    fields = ['user', 'portfolio_site', 'profile_pic', 'job', 'o_date', 'd_date', 'fn', 'ln', 'ads', 'status']
    search_fields = ["user__username", "job", "o_date", "d_date", "fn", "ln", "ads", "status"]

admin.site.register(Item, ItemAdmin)
admin.site.register(OrderItem)
admin.site.register(Order, OrderAdmin)
admin.site.register(Payment)
admin.site.register(Coupon)
admin.site.register(Refund)
admin.site.register(BillingAddress, AddressAdmin)
admin.site.register(ObjectViewed)
admin.site.register(UserProfileInfo, UserProfileInfoAdmin)