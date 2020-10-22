from __future__ import annotations
from enum import Enum
import strawberry
from typing import List


@strawberry.enum
class Flavour(Enum):
    VANILLA = "vanilla"
    STRAWBERRY = "strawberry"
    CHOCOLATE = "chocolate"


@strawberry.type
class IceCream:
    num_scoops: int
    sequence_scoops: List['Flavour']


def makeIceCream():
    return IceCream(num_scoops=4,
                    sequence_scoops=[Flavour.STRAWBERRY,
                                     Flavour.CHOCOLATE,
                                     Flavour.VANILLA,
                                     Flavour.STRAWBERRY])


@strawberry.type
class Query:
    cone: IceCream = strawberry.field(resolver=makeIceCream)

    @strawberry.field
    def another_cone(self) -> IceCream:
        return IceCream(num_scoops=3,
                        sequence_scoops=[Flavour.STRAWBERRY,
                                         Flavour.CHOCOLATE,
                                         Flavour.VANILLA])


schema = strawberry.Schema(query=Query)
