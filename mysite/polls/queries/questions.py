from typing import List

import strawberry

from .. import models
from ..types.question import Question


@strawberry.field
def questions() -> List[Question]:
    queryset = models.Question.objects.all()
    return queryset