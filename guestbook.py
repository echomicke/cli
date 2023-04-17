import sys
import json

FILE_NAME = "guestbook.txt"

def GetFileContents():
    """Returns The contents of the guestbook textfile"""
    with open(FILE_NAME, "r") as f:
        entries = f.read()
    return entries

def ReplaceFileContent(new_entries):
    """Takes in a list and replaces the contents of the guestbook textfile with the list"""
    with open(FILE_NAME, "w") as f:
        f.write('\n'.join(new_entries))
        f.write("\n")

def AddEntry(entry):
    """Adds an entry to the end of a file. Creates a new file if the file is missing"""
    with open(FILE_NAME, "a+") as f:
        f.write(f"{entry}\n")

def PrintEntries():
    """Prints all entries in a file to the console"""
    entries = GetFileContents()
    print(entries)

def EditEntry(index, entry):
    """Replaces an entry in a file with the given entry.\n
    index is the number of the line to be replaced \n
    entry is the data to add to the file"""
    entries = GetFileContents()
    entries = entries.splitlines()
    entries[-int(index)] = entry

    ReplaceFileContent(entries)


def DeleteEntry(index):
    """Deletes an entry in the file \n
    index is the line number(from  the bottom) to be deleted"""
    entries = GetFileContents()
    entries = entries.splitlines()
    entries.pop(-int(index))
    ReplaceFileContent(entries)

def Export():
    "Prints out all the entries in the file in json format and returns it"
    entries = GetFileContents()
    entries = entries.splitlines()
    json_data = json.dumps(entries)
    print (json_data)
    return json_data

def Menu():
    if sys.argv[1] == "new":
        AddEntry(sys.argv[2])

    elif sys.argv[1] == "list":
        PrintEntries()

    elif sys.argv[1] == "edit":
        EditEntry(sys.argv[2], sys.argv[3])
    
    elif sys.argv[1] == "delete":
        DeleteEntry(sys.argv[2])

    elif sys.argv[1] == "export":
        Export()

if __name__ == '__main__':
    Menu()