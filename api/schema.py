import graphene
from graphene_django import DjangoObjectType

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


class Query(graphene.ObjectType):
    book_list = graphene.List(BookType)
    book = graphene.Field(BookType, id=graphene.ID(required=True))

    def resolve_book_list(root, info):
        return Book.objects.all()

    def resolve_book(root, info, id):
        user = info.context.user
        print(user)
        return Book.objects.filter(id=id).first()


schema = graphene.Schema(query=Query)
