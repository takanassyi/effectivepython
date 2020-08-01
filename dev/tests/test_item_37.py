from src.item_37 import SimpleGradebook


def test_simplegradebook():
    book = SimpleGradebook()
    book.add_student('Isaac Newton')
    book.report_grade('Isaac Newton', 90)
    book.report_grade('Isaac Newton', 95)
    book.report_grade('Isaac Newton', 85)

    score = book.average_grade('Isaac Newton')
    assert score == 80.0
