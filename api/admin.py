from django.contrib import admin

from api.models import *


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "author",
        "publisher",
        "publication_date",
        "isbn",
        "price",
        "pages",
    ]


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = [
        "first_name",
        "last_name",
        "age",
        "email",
        "biography",
        "birth_date",
        "nationality",
        "website",
    ]


@admin.register(Publisher)
class PublisherAdmin(admin.ModelAdmin):
    list_display = ["name", "address", "phone_number", "website"]
