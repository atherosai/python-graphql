import graphene
from server.schema.LevenshteinDistanceInputType import LevenshteinDistanceInput
from server.schema.LevenshteinDistancePayload import LevenshteinDistancePayload
from server.text_analytics.levenshtein_distance import calculate_levenshtein_distance

class LevenshteinDistanceMutation(graphene.Mutation):
    class Arguments:
        input = LevenshteinDistanceInput(required=True)

    Output = LevenshteinDistancePayload

    def mutate(self, info, input):
        return {
          "levenshtein_distance": calculate_levenshtein_distance(input)
        }