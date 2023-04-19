import graphene

class LevenshteinDistancePayload(graphene.ObjectType):
    levenshtein_distance = graphene.Float()