import graphene
from django.core.files.storage import default_storage
from graphene_django import DjangoObjectType
from graphene_file_upload.scalars import Upload

from api.models import Author, Book, Publisher


class BookType(DjangoObjectType):
    class Meta:
        model = Book
        fields = "__all__"

    def resolve_cover_image(self, info):
        return self.cover_image.url if self.cover_image else None


class AuthorType(DjangoObjectType):
    class Meta:
        model = Author
        fields = "__all__"


class PublisherType(DjangoObjectType):
    class Meta:
        model = Publisher
        fields = "__all__"


class UploadFileMutation(graphene.Mutation):
    class Arguments:
        file = Upload(required=True)

    success = graphene.Boolean()

    def mutate(self, info, file, **kwargs):
        file_name = default_storage.save(file.name, file)
        return UploadFileMutation(success=True)


class Query(graphene.ObjectType):
    book_list = graphene.List(BookType)
    book = graphene.Field(BookType, id=graphene.ID(required=True))

    def resolve_book_list(root, info):
        return Book.objects.all()

    def resolve_book(root, info, id):
        user = info.context.user
        print(user)
        return Book.objects.filter(id=id).first()


class Mutate(graphene.ObjectType):
    upload_file = UploadFileMutation.Field()


schema = graphene.Schema(query=Query, mutation=Mutate)
