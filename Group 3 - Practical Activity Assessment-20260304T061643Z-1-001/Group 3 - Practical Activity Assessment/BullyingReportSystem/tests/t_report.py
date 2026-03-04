import sys
import os
import pytest

# Allow access to src folder
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))

from t_report import Report # type: ignore


def test_valid_report_creation():
    report = Report("Bullying incident in hallway")
    assert report.message == "Bullying incident in hallway"
    assert report.status == "Pending"


def test_empty_report_should_fail():
    with pytest.raises(ValueError):
        Report("")


def test_status_update():
    report = Report("Bullying case")
    report.update_status("Reviewed")
    assert report.status == "Reviewed"


def test_invalid_status_update():
    report = Report("Bullying case")
    with pytest.raises(ValueError):
        report.update_status("WrongStatus")


def test_anonymous_report():
    report = Report("Bullying case")
    assert report.reporter_name is None
