animals = ["fly", "spider", "bird", "cat", "dog", "goat", "cow", "horse"]

opening_lines = ["I know an old lady who swallowed a spider. It wriggled and jiggled and tickled inside her.\n",
                "I know an old lady who swallowed a bird. How absurd to swallow a bird!\n",
                "I know an old lady who swallowed a cat. Imagine that, to swallow a cat!\n",
                "I know an old lady who swallowed a dog. What a hog, to swallow a dog!\n",
                "I know an old lady who swallowed a goat. Just opened her throat and swallowed a goat!\n",
                "I know an old lady who swallowed a cow. I don't know how she swallowed a cow!\n",]
               
stack_lines = ["She swallowed the cow to catch the goat.\n",
            "She swallowed the goat to catch the dog.\n",
            "She swallowed the dog to catch the cat.\n",
            "She swallowed the cat to catch the bird.\n",
            "She swallowed the bird to catch the spider that wriggled and jiggled and tickled inside her.\n",
            "She swallowed the spider to catch the fly.\n"
            "I don't know why she swallowed that fly! Perhaps she'll die!\n"]

def intro():
    line = """There was an old lady who swallowed a fly, 
            I don't know why she swallowed the fly, 
            Perhaps she'll die.\n"""
    print(line)

def build_verse():
    #for index in range(len(animal_list)):
        #line = f'She swallowed the {animal_list[index]} to catch the {animal_list[index-1]} I dont know why she swallowed the fly. Perhaps she will die!'
        #print(line)
        print(opening_lines[0], stack_lines[-1], opening_lines[1], stack_lines[-2], stack_lines[-1], opening_lines[2], stack_lines[-3], stack_lines[-2], stack_lines[-1], opening_lines[3], stack_lines[-4], stack_lines[-3], stack_lines[-2], stack_lines[-1], opening_lines[4], stack_lines[-5], stack_lines[-4], stack_lines[-3], stack_lines[-2], stack_lines[-1], opening_lines[5], stack_lines[-6], stack_lines[-5], stack_lines[-4], stack_lines[-3], stack_lines[-2], stack_lines[-1],)

def outro():
    line = "There was an old lady who swallowed a horse, She died of course!"
    print(line)

def song():
    intro()
    build_verse()
    outro()

song()
