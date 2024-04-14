import os
import subprocess
import pytest

from n2t.runner.cli import run_vm_translator

_TEST_PROGRAMS = [("FunctionCalls", "SimpleFunction"),
                  ("FunctionCalls", "NestedCall"),
                  ("FunctionCalls", "FibonacciElement"),
                  ("FunctionCalls", "StaticsTest"),
                  ("ProgramFlow", "BasicLoop"),
                  ("ProgramFlow", "FibonacciSeries")]


@pytest.mark.parametrize("test_file", _TEST_PROGRAMS)
def test_run_emulator_and_check_output(test_file):
    directory_name = test_file[0] + "/" + test_file[1]
    tst_file = directory_name + "/" + test_file[1] + ".tst"

    script_dir = os.path.dirname(os.path.abspath(__file__))
    bat_file_path = os.path.join(script_dir, "../../../nand2tetris/tools/CPUEmulator.bat")
    test_file_path = os.path.join(script_dir, "../../../nand2tetris/projects/8/", tst_file)
    directory = os.path.join(script_dir, "../../../nand2tetris/projects/8/", directory_name)

    run_vm_translator(directory)

    command = f'"{bat_file_path}" "{test_file_path}"'
    process = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output = process.communicate()[0].decode("utf-8")

    assert "end of script - comparison ended successfully" in output.lower()
