import sys
import json

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
    entries[-int(index)] = entry

    with open(FILE_NAME, "w") as f:
        f.write('\n'.join(entries))
        f.write("\n")

def DeleteEntry(index):
    """Deletes an entry in the file \n
    index is the line number(from  the bottom) to be deleted"""
    f = open(FILE_NAME)
    entries = f.read()
    f.close()
    entries = entries.splitlines()
    entries.pop(-int(index))

    with open(FILE_NAME, "w") as f:
        f.write('\n'.join(entries))
        f.write("\n")

def Export():
    "Prints out all the entries in the file in json format and returns it"
    with open(FILE_NAME, "r") as f:
        entries = f.read()
    entries = entries.splitlines()
    entries.pop(len(entries)-1)
    json_data = json.dumps(entries)
    print (json_data)
    return json_data

def Menu():
    if sys.argv[1] == "new":
        AddEntry(sys.argv[2])

    elif sys.argv[1] == "list":
        GetAllEntries()

    elif sys.argv[1] == "edit":
        EditEntry(sys.argv[2], sys.argv[3])
    
    elif sys.argv[1] == "delete":
        DeleteEntry(sys.argv[2])

    elif sys.argv[1] == "export":
        Export()

if __name__ == '__main__':
    Menu()