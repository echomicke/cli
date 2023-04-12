import guestbook as Guestbook

class TestClass:

    def test_Add_Entry():
        entry = "this is a test entry"
        Guestbook.AddEntry(entry)

        with open('guestbook.txt', 'r') as gb:
            entries = gb.read()
            if entry in entries:
                assert True
        