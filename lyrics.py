# make a function for opening sentance
# new animal is introduced with each series.
# each series has both unique phrases and repeating phrases.
# make a function that calls repeated phrases with each series.

animals = [
    "There was an old lady who swallowed a fly, I dont why know she swallowed that fly, perhaps she will die."
    "There was an old lady who swallowed a spider, It wiggled and jiggled and tickled inside her."
    "There was an old lady who swallowed a bird, How absurd, to swallow a bird."
    "There was an old lady who swallowed a cat, Imagine that, she swallowed a cat."
    "There was an old lady who swallowed a dog, What a hog, to swallow a dog."
    "There was an old lady who swallowed a goat, She just opened her throat and swallowed a goat."
    "There was an old lady who swallowed a cow, I dont know how she swallowed a cow."
    "There was an old lady who swallowed a horse, Shes dead of course."]
    
    #intro = "There was an old lady who swallowed a"

# def intro():
#     intro = line_1
#     line_1 = ("There was an old lady who swallowed a")
#     print(intro)
    


def play(animal):
    for animal in animals:
        print(f' {animal} ')
        

play(animals)