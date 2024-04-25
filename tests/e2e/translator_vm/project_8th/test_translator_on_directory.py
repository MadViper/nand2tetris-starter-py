import os
from pathlib import Path

import pytest

from tests.e2e.conftest import run_vm_translator_test

_TEST_PROGRAMS = [
    ("FunctionCalls", "SimpleFunction"),
    ("FunctionCalls", "NestedCall"),
    ("FunctionCalls", "FibonacciElement"),
    ("FunctionCalls", "StaticsTest"),
    ("ProgramFlow", "BasicLoop"),
    ("ProgramFlow", "FibonacciSeries"),
]


@pytest.mark.parametrize("test_file", _TEST_PROGRAMS)
def test_run_emulator_and_check_output(
    test_file: tuple[str, str], cpu_emulator_bat: Path, projects_directory: Path
) -> None:
    project_part, directory_name = test_file
    projects_directory_path = os.path.join(
        projects_directory, "8", project_part, directory_name
    )

    run_vm_translator_test(
        cpu_emulator_bat, projects_directory_path, directory_name + ".tst"
    )
