from marshmallow import post_load
from marshmallow import fields
from marshmallow import Schema

from author.models import User


class AuthorSchema(Schema):
    class Meta(object):
        model = User

    id = fields.Integer()
    email = fields.String()
    username = fields.String()
    first_name = fields.String()
    last_name = fields.String()

    @post_load
    def update_or_create(self, data, *args, **kwargs):
        author, _ = User.objects.update_or_create(
            id=data.pop("id", None), defaults=data
        )
        return author
