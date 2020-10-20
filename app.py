import strawberry
from typing import List


@strawberry.type
class TodoType:
    name: str
    done: bool


def getTodos():
    return [
        TodoType(name="#1", done=True),
        TodoType(name="#2", done=True),
        TodoType(name="#3", done=False),
    ]


@strawberry.type
class Query:
    TodoTypes: List[TodoType] = strawberry.field(resolver=getTodos)


schema = strawberry.Schema(query=Query)
