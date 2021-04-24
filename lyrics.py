# make a function for each verse
# new animal is introduced with each verse.
# each series has both unique phrases and repeating phrases.
# make a function that calls repeated phrases with each series.

animals = ["fly", "spider", "bird", "cat", "dog", "goat", "cow", "horse"]

def build_verse(animal_list):
    for index in range(len(animal_list)):
        line = f'She swallowed the {animal_list[index]} to catch the {animal_list[index-1]}'
        print(line)
build_verse(animals)

def title():
    line = "I know an old lady"
    print(line)

def intro():
    line = """There was an old lady who swallowed a fly, 
            I don't know why she swallowed the fly, 
            Perhaps she'll die."""
    print(line)

def verse_2():
    line = """There was an old lady who swallowed a spider, 
            that wiggled and jiggled inside her. She swallowed the spider to catch the fly. 
            I don't know why she swallowed that fly, 
            Perhaps she'll die."""
    print(line)

def verse_3():
    line = """There was an old lady who swallowed a bird,
            How absurd to swallow a bird.
            She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her,
            She swallowed the spider to catch the fly,
            I don't know why she swallowed that fly,
            Perhaps she'll die."""
    print(line)

def verse_4():
    line = """There was an old lady who swallowed a cat,
            Imagine that to swallow a cat.
            She swallowed the cat to catch the bird,
            She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her,
            She swallowed the spider to catch the fly,
            I don't know why she swallowed that fly,
            Perhaps she'll die."""
    print(line)

def verse_5():
    line = """There was an old lady who swallowed a dog,
            What a hog to swallow a dog.
            She swallowed the dog to catch the cat,
            She swallowed the cat to catch the bird,
            She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her,
            She swallowed the spider to catch the fly,
            I don't know why she swallowed that fly,
            Perhaps she'll die."""
    print(line)

def verse_6():
    line = """I know an old lady who swallowed a goat.
            Just opened her throat and swallowed a goat!
            She swallowed the goat to catch the dog.
            She swallowed the dog to catch the cat.
            She swallowed the cat to catch the bird.
            She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.
            She swallowed the spider to catch the fly.
            I don't know why she swallowed the fly. 
            Perhaps she'll die."""
    

def verse_7():
    line = """I know an old lady who swallowed a cow.
            I don't know how she swallowed a cow!
            She swallowed the cow to catch the goat.
            She swallowed the goat to catch the dog.
            She swallowed the dog to catch the cat.
            She swallowed the cat to catch the bird.
            She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.
            She swallowed the spider to catch the fly.
            I don't know why she swallowed the fly. 
            Perhaps she'll die."""
    

def outro():
    line = """There was an old lady who swallowed a horse,
            She died of course!"""

def song():
    title()
    intro()
    verse_2()
    verse_3()
    verse_4()
    verse_5()
    verse_6()
    verse_7()
    outro()

song()