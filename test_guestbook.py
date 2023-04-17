import guestbook as Guestbook
import json
import io
import sys

class TestClass:

    def test_get_file_content(self):
        with open("guestbook.txt", "r") as f:
            file_contents = f.read()
        assert file_contents == Guestbook.GetFileContents()
    
    def test_replace_file_content(self):
        new_entry = ["entry one", "entry two", "entry three", "entry 8"]
        Guestbook.ReplaceFileContent(new_entry)
        with open("guestbook.txt", "r") as f:
            entries = f.read()
        assert new_entry == entries.splitlines()

    def test_Add_Entry(self):
        entry = "this is a test entry"
        Guestbook.AddEntry(entry)

        with open('guestbook.txt', 'r') as gb:
            entries = gb.read()
            if entry in entries:
                assert True
    
    def test_Print_All_Entries(self):
        capturedOutput = io.StringIO()
        sys.stdout = capturedOutput
        Guestbook.PrintEntries()
        assert capturedOutput.getvalue()
        sys.stdout = sys.__stdout__ 
    
    def test_Edit_Entry(self):
        entry = "This entry was edited2"
        Guestbook.EditEntry(1, entry)
        with open('guestbook.txt', 'r') as f:
            entries = f.read()
        entries = entries.splitlines()

        assert entry == entries[-1]
            
    def test_Delete_Entry(self):
        indx = 1
        entry = "Entry to be deleted"
        Guestbook.AddEntry(entry)
        Guestbook.DeleteEntry(indx)

        with open('guestbook.txt', 'r') as f:
            entries = f.read()
        
        entries = entries.splitlines()
        assert entries[len(entries)-1] != entry

    def test_Export_to_json(self):
        with open("guestbook.txt", "r") as f:
            entries = f.read()
        entries = entries.splitlines()
        json_data = json.dumps(entries)

        assert json_data == Guestbook.Export()