import os

#Informing the Code of the File Path and Where to Place the New File
file_path = os.path.join("docs","poem_original.txt")
new_file_path = os.path.join("docs","poem_new.txt")

#Creating the Function to Read The Poem
def read_poem(file_path):
    #The code reads the poem
    try:
        with open(file_path, "r") as f:
            lines = f.readlines()
        return [line.strip() for line in lines]
    #If their is no such file, the code will handle the error:
    except FileNotFoundError:
        print(f"Error: The file: '{file_path}' was not found.")
        return[]
#Creating the Function to Write the Poem Appropriately
def write_poem(new_file_path, lines):
    try:
        with open(new_file_path, "w") as f:
            for line in lines:
                f.write(line + "\n")
    except Exception as e:
        print(f"Error: {e}")
#Creating the Function to change parts of the Poem
def append_poem(new_file_path, extra_lines):
    try:
        with open(new_file_path, "a") as f:
            for line in extra_lines:
                f.write(line + "\n")
    except Exception as e:
        print(f"Error: {e}")

#Here is where it gets interesting, the poem will run backwards and some of the words will change
def mix_poem(poem_lines):
    poem_lines.reverse()
    for i in range(len(poem_lines)):
        poem_lines[i] = poem_lines[i].replace("seed", "person")
        poem_lines[i] = poem_lines[i].replace("said", "whispered")
    return poem_lines

#A function created just to ensure that the Poem is printed back properly
def print_poem(poem_lines):
    for line in poem_lines:
        print(line)

#Now, We put it all together!
def main():
    #Can't do anything to the poem until we read it.
    poem_lines = read_poem(file_path)
    print("Original Poem:")
    print_poem(poem_lines)
    #Let's Mix it up!
    mixed_poem = mix_poem(poem_lines.copy())

    print("\nMixed Poem:")
    print_poem(mixed_poem)

    write_poem(new_file_path, mixed_poem)

    #Guilty as charged! I mixed up the poem!
    extra_lines = ["---",
                   "Mixed up By: Etta",
                   "I changed the order and switched the word seed to person and the word said to whispered"]
    append_poem(new_file_path, extra_lines)
    print("\nMixed Poem with Appended Lines:")

    #Let's not forget to print the final poem.
    final_version = read_poem(new_file_path)
    print_poem(final_version)

#and Run the Program from Main
if __name__ == "__main__":
    main()