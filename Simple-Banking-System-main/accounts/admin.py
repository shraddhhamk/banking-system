from django.contrib import admin

from .models import BankAccountType, User, UserAddress, UserBankAccount


#admin.site.register(BankAccountType)
#admin.site.register(User)
#admin.site.register(UserAddress)
#admin.site.register(UserBankAccount)



@admin.register(BankAccountType)
class BankAccountTypeModel(admin.ModelAdmin):
    list_filter = ('name','maximum_withdrawal_amount','annual_interest_rate','interest_calculation_per_year')
    list_display = ('id','name','maximum_withdrawal_amount','annual_interest_rate','interest_calculation_per_year')


@admin.register(UserAddress)
class UserAddressModel(admin.ModelAdmin):
    list_filter = ('street_address','city','postal_code','country','user')
    list_display = ('id','street_address','city','postal_code','country','user')


@admin.register(User)
class UserModel(admin.ModelAdmin):
    list_filter = ('last_login','is_superuser','first_name','last_name','is_staff','is_active','date_joined','email','groups','user_permissions')
    list_display = ('id','password','last_login','is_superuser','first_name','last_name','is_staff','is_active','date_joined','email')


@admin.register(UserBankAccount)
class UserBankAccountModel(admin.ModelAdmin):
    list_filter = ('account_no','gender','birth_date','balance','interest_start_date','initial_deposit_date','account_type','user')
    list_display = ('id','account_no','gender','birth_date','balance','interest_start_date','initial_deposit_date','account_type','user')