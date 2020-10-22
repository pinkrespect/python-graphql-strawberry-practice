from enum import Enum
import strawberry


@strawberry.enum
class IceCreamFlavour(Enum):
    VANILLA = "vanilla"
    STRAWBERRY = "strawberry"
    Chocolate = "CHOCOLATE"


@strawberry.type
class Cone:
    flavour: IceCreamFlavour
    num_scoops: int


@strawberry.type
class Query:
    @strawberry.field
    def cone(self, info) -> Cone:
        return Cone(flavour=IceCreamFlavour.STRAWBERRY, num_scoops=4)


schema = strawberry.Schema(query=Query)
