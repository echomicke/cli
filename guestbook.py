FILE_NAME = "guestbook.txt"

def AddEntry(entry):
    with open(FILE_NAME, "a+") as f:
        f.write(f"{entry}\n")