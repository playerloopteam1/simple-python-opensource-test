import pytest
from expense_tracker import (
    ExpenseTracker,
    main,
)


def test_default_properties():
    """
    Test that a newly created ExpenseTracker instance has the default properties.
    Specifically, verify that the 'expenses' list is empty and that the 'categories'
    set contains the expected default categories: "food", "transport", "utilities",
    "entertainment", and "other".
    """
    tracker = ExpenseTracker()
    assert tracker.expenses == []
    expected_categories = {"food", "transport", "utilities", "entertainment", "other"}
    assert tracker.categories == expected_categories


def test_main_output(capsys):
    """
    Test that when main() is called, it prints 'nothing here yet' to stdout.
    """
    main()
    captured = capsys.readouterr()
    assert captured.out == "nothing here yet\n"


def test_add_expense():
    """
    Test that an expense can be directly added to the 'expenses' list of an ExpenseTracker instance.
    This simulates adding an expense record (e.g., a dictionary) to verify that the list is mutable
    and retains the newly added expense.
    """
    tracker = ExpenseTracker()
    expense = {"amount": 50, "category": "food"}
    tracker.expenses.append(expense)
    assert tracker.expenses == [expense]


def test_instance_independence():
    """
    Test that two ExpenseTracker instances have independent 'expenses' lists and 'categories' sets.
    Modifying one instance does not affect the properties of the other instance.
    """
    tracker1 = ExpenseTracker()
    tracker2 = ExpenseTracker()
    tracker1.expenses.append({"amount": 20, "category": "transport"})
    tracker1.categories.add("new_category")
    assert tracker2.expenses == []
    expected_categories = {"food", "transport", "utilities", "entertainment", "other"}
    assert tracker2.categories == expected_categories


def test_instance_unique_objects():
    """
    Test that each ExpenseTracker instance has its own unique 'expenses' list and 'categories' set.
    This helps to confirm that modifications in one instance do not affect the other due to
    shared mutable objects.
    """
    tracker1 = ExpenseTracker()
    tracker2 = ExpenseTracker()
    assert tracker1.expenses is not tracker2.expenses
    assert tracker1.categories is not tracker2.categories


def test_property_types():
    """
    Test that a newly created ExpenseTracker instance has properties of the correct types.
    Specifically, verify that 'expenses' is a list and 'categories' is a set.
    """
    tracker = ExpenseTracker()
    assert isinstance(tracker.expenses, list), "'expenses' should be a list"
    assert isinstance(tracker.categories, set), "'categories' should be a set"


def test_append_different_types():
    """
    Test that various types of objects can be appended to the 'expenses' list
    without errors, since the ExpenseTracker class does not enforce any type validation
    for the expense records.
    """
    tracker = ExpenseTracker()
    sample_items = [42, "A random expense", [1, 2, 3], {"nested": "dict"}]
    for item in sample_items:
        tracker.expenses.append(item)
    assert tracker.expenses == sample_items


def test_expenses_order():
    """
    Test that the 'expenses' list maintains the insertion order.
    This test appends several expense records and verifies the order is preserved.
    """
    tracker = ExpenseTracker()
    expense1 = {"amount": 30, "category": "food"}
    expense2 = {"amount": 15, "category": "transport"}
    expense3 = {"amount": 60, "category": "utilities"}
    tracker.expenses.append(expense1)
    tracker.expenses.append(expense2)
    tracker.expenses.append(expense3)
    expected_order = [expense1, expense2, expense3]
    assert tracker.expenses == expected_order


def test_main_called_twice(capsys):
    """
    Test that calling main() twice separately prints 'nothing here yet'
    each time to stdout, ensuring consistent behavior on multiple calls.
    """
    main()
    captured_first = capsys.readouterr()
    assert captured_first.out == "nothing here yet\n"
    main()
    captured_second = capsys.readouterr()
    assert captured_second.out == "nothing here yet\n"


def test_expenses_order_after_removal():
    """
    Test that after removing an expense, the order of the remaining expenses is preserved.
    This test appends three expense records to the tracker, removes the middle one, and verifies that
    the order of the remaining records is as expected.
    """
    tracker = ExpenseTracker()
    expense1 = {"amount": 40, "category": "food"}
    expense2 = {"amount": 25, "category": "transport"}
    expense3 = {"amount": 15, "category": "utilities"}
    tracker.expenses.append(expense1)
    tracker.expenses.append(expense2)
    tracker.expenses.append(expense3)
    tracker.expenses.remove(expense2)
    expected_order = [expense1, expense3]
    assert tracker.expenses == expected_order
