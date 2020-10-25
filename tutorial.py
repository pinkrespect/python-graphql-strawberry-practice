from __future__ import annotations
import strawberry
from typing import List


@strawberry.type
class date:
    start: int
    end: int


@strawberry.type
class todo:
    name: str
    done: bool
    date: date


@strawberry.input
class sayEmail:
    email: str


def getTodos():
    return [
        todo(name="#1", done=True, date=date(start=1, end=2)),
        todo(name="#2", done=True, date=date(start=2, end=3)),
        todo(name="#3", done=False, date=date(start=3, end=0)),
    ]


@strawberry.type
class Query:
    todos: List[todo] = strawberry.field(resolver=getTodos)


@strawberry.type
class Mutation:
    @strawberry.mutation
    def sendEmail(self, info, input: sayEmail) -> str:
        return f"sending email to {input.email}"


schema = strawberry.Schema(query=Query, mutation=Mutation)

query = 'mutation { sendEmail(input: { email: "이메일" }) }'
result = schema.execute_sync(query)
print(result)
