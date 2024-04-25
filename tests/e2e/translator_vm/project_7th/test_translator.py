import os
from pathlib import Path

import pytest

from tests.e2e.conftest import run_vm_translator_test

_TEST_PROGRAMS = [
    ("MemoryAccess", "BasicTest"),
    ("MemoryAccess", "PointerTest"),
    ("MemoryAccess", "StaticTest"),
    ("StackArithmetic", "SimpleAdd"),
    ("StackArithmetic", "StackTest"),
]


@pytest.mark.parametrize("test_file", _TEST_PROGRAMS)
def test_run_emulator_and_check_output(
    test_file: tuple[str, str], cpu_emulator_bat: Path, projects_directory: Path
) -> None:
    project_part, directory_name = test_file
    projects_directory_path = os.path.join(
        projects_directory, "7", project_part, directory_name
    )

    tst_file = directory_name + ".tst"
    vm_file = directory_name + ".vm"
    run_vm_translator_test(cpu_emulator_bat, projects_directory_path, tst_file, vm_file)
