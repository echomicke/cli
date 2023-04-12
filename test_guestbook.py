import guestbook as Guestbook
import json

class TestClass:

    def test_Add_Entry(self):
        entry = "this is a test entry"
        Guestbook.AddEntry(entry)

        with open('guestbook.txt', 'r') as gb:
            entries = gb.read()
            if entry in entries:
                assert True
    
    def test_Get_All_Entries(self):
        entries = ""
        with open('guestbook.txt', 'r') as f:
            entries = f.read()
        assert entries == Guestbook.GetAllEntries()
    
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
        entries = Guestbook.GetAllEntries()
        json_data = json.dumps(entries.pop(len(entries)-1))

        assert json_data == Guestbook.Export()