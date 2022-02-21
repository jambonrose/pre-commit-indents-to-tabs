"""Test indent to tabs conversion function"""
from io import BytesIO

from pytest import mark, param

from indents_to_tabs.convert import convert_indents
from indents_to_tabs.pass_fail_constants import FAIL, PASS

from .file_utils import load_file, load_file_to_buffer


@mark.parametrize(
    "file_name",
    [
        param("tabs.tf", id="tf_tabs"),
        param("indent_error_tabs.tf", id="tf_indent_error_tabs"),
    ],
)
def test_convert_indents_no_changes(file_name: str) -> None:
    """Does converting the input file result in the expected file?"""
    indent_size = 2  # should not matter in files with tabs
    expected = load_file(file_name)
    buffer = BytesIO(expected)

    return_code = convert_indents([buffer], indent_size)
    buffer.seek(0)

    assert buffer.read() == expected
    assert return_code == PASS


@mark.parametrize(
    "input_file_name,expected_file_name,indent_size",
    [
        param("spaces_2.tf", "tabs.tf", 2, id="tf_2"),
        param("spaces_4.tf", "tabs.tf", 4, id="tf_4"),
        param(
            "indent_error.tf", "indent_error_tabs.tf", 2, id="tf_indent_error"
        ),
    ],
)
def test_convert_indents_changes(
    input_file_name: str, expected_file_name: str, indent_size: int
) -> None:
    """Does converting the input file result in the expected file?"""
    buffer = load_file_to_buffer(input_file_name)
    expected = load_file(expected_file_name)

    return_code = convert_indents([buffer], indent_size)
    buffer.seek(0)

    assert buffer.read() == expected
    assert return_code == FAIL
