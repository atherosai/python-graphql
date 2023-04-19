import nltk

def calculate_levenshtein_distance(input):
    return nltk.edit_distance(s1=input["s1"], s2=input["s2"], substitution_cost=input["substitution_cost"], transpositions=input["transpositions"])