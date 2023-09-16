from typing import List, Annotated

import strawberry
import strawberry_django

from .. import models

LazyChoice = Annotated["Choice", strawberry.lazy(
    "polls.types.choice"
)]


@strawberry_django.type(models.Question)
class Question:
    id: strawberry.auto
    choices: List[LazyChoice]