FILE_NAME = "guestbook.txt"

def AddEntry(entry):
    """Adds an entry to the end of a file. Creates a new file if the file is missing"""
    with open(FILE_NAME, "a+") as f:
        f.write(f"{entry}\n")

def GetAllEntries():
    """Prints all entries in a file to the console"""
    with open(FILE_NAME, "r") as f:
        entries = f.read()
    print(entries)
    return entries

def EditEntry(index, entry):
    """Replaces an entry in a file with the given entry.\n
    index is the number of the line to be replaced \n
    entry is the data to add to the file"""
    f = open(FILE_NAME)
    entries = f.read()
    f.close()
    entries = entries.splitlines()
    entries[int(-index)] = entry

    with open(FILE_NAME, "w") as f:
        f.write('\n'.join(entries))
        f.write("\n")