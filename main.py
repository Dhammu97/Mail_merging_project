PLACEHOLDER = "[name]"

with open("./mail_merging_project/input/names/invited_names.txt") as invited_name:
    names = invited_name.readlines()

with open("./mail_merging_project/input/letters/starting_letter.txt") as letter:
    letter_contain = letter.read()

    for name in names:
        strip_name = name.strip()
        new_name = letter_contain.replace(PLACEHOLDER, strip_name)

        with open(f"./mail_merging_project/output/letter_of_{strip_name}", mode="w") as complete_letter:
            complete_letter.write(new_name)   
    