import os

DOCS_DIR = "docs" #name the docs folder
PATH = "" #create a global PATH
poem = ["Roses are Red,\n",
    "Violets are Blue,\n",
    "Some Poems Rhyme, \n",
    "But this one doesn't! \n"] #put in the original poem

def write_poem():
    global poem
    PATH = os.path.join(DOCS_DIR, "best_poem.txt")
    print(PATH)
    #write the original poem in the doc
    with open(PATH, "w") as f:
        f.write(f"This poem has a surprise ending!\n")
        f.writelines(poem)


def append_poem():
    PATH = os.path.join(DOCS_DIR, "best_poem.txt")
    NEW_PATH = os.path.join(DOCS_DIR, "best_poem2.txt")
    with open(PATH, "r") as f:
       lines = f.readlines()
    lines[4] = "and This One Does Too!\n"
    with open(NEW_PATH, "w") as f:
        f.writelines(lines)
    #edit the poem to fix the last line


def read_poem(PATH):
    PATH = os.path.join(DOCS_DIR, "best_poem.txt")
    with open(PATH, "r") as f:
        for lines in f:
            print(lines.strip().replace("\n", ""))
    #read the poem

def main():

#run the whole program together

    write_poem()
    print("Original Poem:")
    print("".join(poem))

    append_poem()
    print("\nUpdated Poem:")
    read_poem(os.path.join(DOCS_DIR, "best_poem2.txt"))

    print(f"I like this poem because it does the unexpected.")
    print(f"You expect it to rhyme and then it doesn't! ")
    print(f"But once you edit it, then it does rhyme. ")

if __name__ == "__main__":
    main()