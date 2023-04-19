import graphene

class LevenshteinDistanceInput(graphene.InputObjectType):
    s1 = graphene.String(required=True)
    s2 = graphene.String(required=True)
    substitution_cost = graphene.Int(default_value=1)
    transpositions = graphene.Boolean(default_value=True) 
