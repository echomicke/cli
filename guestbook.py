FILE_NAME = "guestbook.txt"

def AddEntry(entry):
    with open(FILE_NAME, "a+") as f:
        f.write(f"{entry}\n")

def GetAllEntries():
    entries = ""
    with open(FILE_NAME, "r") as f:
        entries = f.read()
    print(entries)
    return entries