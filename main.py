with open("books/frankenstein.txt") as f:
    file_contents = f.read()
    file_contents = file_contents.lower()

def main():
    words = file_contents.split()
    numCharacters = {}
    total = len(words)
    for character in words:
        for i in character:
            if i not in numCharacters:
                numCharacters[i] = 1
            else:
                numCharacters[i] += 1

    listing = []
    for key, value in numCharacters.items():
        listing.append({"char": key, "num": value})
    
    def sort_on(dict):
        return dict["num"]
    
    listing.sort(reverse=True, key=sort_on)

    print("Begin report of book Frankenstein")
    print(f"{total} words found in the document")
    for dict in listing:
        if not dict["char"].isalpha():
            continue
        print(f"The {dict["char"]} character was found {dict["num"]} times")



main()