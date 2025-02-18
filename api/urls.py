from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from graphene_file_upload.django import FileUploadGraphQLView

from api.schema import schema
from api.views import index

urlpatterns = [
    path(
        "",
        csrf_exempt(FileUploadGraphQLView.as_view(schema=schema, graphiql=True)),
        name="api",
    ),
    path("index/", index, name="index"),
]
