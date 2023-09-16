from typing import Annotated

import strawberry
import strawberry_django

from .question import Question
from .. import models

LazyQuestion = Annotated["Question", strawberry.lazy(
    "polls.types.question"
)]

@strawberry_django.type(models.Choice)
class Choice:
    id: strawberry.auto
    choice_text: str
    votes: int
    question: LazyQuestion