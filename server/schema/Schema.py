import graphene
from server.schema.levenshtein_calc import LevenshteinDistanceMutation

class Query(graphene.ObjectType):
    healthcheck = graphene.Boolean(required=True)

    def resolve_healthcheck(self, info):
        return True


class Mutation(graphene.ObjectType):
    levenshtein_distance = LevenshteinDistanceMutation.Field()

Schema = graphene.Schema(query=Query, mutation=Mutation)