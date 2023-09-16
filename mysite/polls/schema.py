from typing import List

import strawberry
import strawberry_django
from django.conf import settings
from strawberry_django import auth
from strawberry_django.optimizer import DjangoOptimizerExtension

from . import models
from .queries.questions import questions

@strawberry_django.type(models.Question)
class Question:
    id: strawberry.auto

@strawberry.type
class Query:
    questions = questions

@strawberry.type
class Mutation:
    logout = auth.logout()


schema = strawberry.Schema(
    query=Query,
    mutation=Mutation,
    extensions=[
        DjangoOptimizerExtension,
    ]
    if settings.DEBUG
    else [
        DjangoOptimizerExtension,
    ],
)
