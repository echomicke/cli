import guestbook as Guestbook

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
        entry = "This entry was edited"
        Guestbook.EditEntry(1, entry)
        with open('guestbook.txt', 'r') as f:
            entries = f.read()
        entries = entries.splitlines()
        assert entry == entries[1]
            
        