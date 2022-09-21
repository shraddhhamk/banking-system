from django.contrib import admin

from transactions.models import Transaction

@admin.register(Transaction)
class TransactionModel(admin.ModelAdmin):
    list_filter = ('amount','balance_after_transaction','transaction_type','timestamp','account')
    list_display = ('id','amount','balance_after_transaction','transaction_type','timestamp','account')
