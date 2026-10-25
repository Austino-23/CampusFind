from django.contrib import admin
from .models import Item, Claim

@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'report_type', 'category', 'location', 'reported_by', 'is_resolved', 'created_at')
    list_filter = ('report_type', 'category', 'is_resolved')
    search_fields = ('name', 'location', 'description', 'reported_by__username')

@admin.register(Claim)
class ClaimAdmin(admin.ModelAdmin):
    list_display = ('item', 'claimant', 'status', 'created_at')
    list_filter = ('status',)
