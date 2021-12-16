import json

from marshmallow import ValidationError
from django.views.generic import View

from author.models import User
from author.schemas import AuthorSchema
from techtest.utils import json_response


class AuthorListView(View):
    def get(self, request, *args, **kwargs):
        return json_response(AuthorSchema().dump(User.objects.all(), many=True))

    def post(self, request, *args, **kwargs):
        try:
            region = AuthorSchema().load(json.loads(request.body))
        except ValidationError as e:
            return json_response(e.messages, 400)
        return json_response(AuthorSchema().dump(region), 201)


class AuthorView(View):
    def dispatch(self, request, author_id, *args, **kwargs):
        try:
            self.author = User.objects.get(pk=author_id)
        except User.DoesNotExist:
            return json_response({"error": "No User matches the given query"}, 404)
        self.data = request.body and dict(json.loads(request.body), id=self.author.id)
        return super(AuthorView, self).dispatch(request, *args, **kwargs)

    def get(self, request, *args, **kwargs):
        return json_response(AuthorSchema().dump(self.author))

    def put(self, request, *args, **kwargs):
        try:
            self.author = AuthorSchema().load(self.data)
        except ValidationError as e:
            return json_response(e.messages, 400)
        return json_response(AuthorSchema().dump(self.author))

    def delete(self, request, *args, **kwargs):
        self.author.delete()
        return json_response()