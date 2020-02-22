#
# Copyright (c) 2017-2019 NVIDIA CORPORATION. All rights reserved.
# This file is part of webloader (see TBD).
# See the LICENSE file for licensing terms (BSD-style).
#

import os
import subprocess


PYTHON3 = os.environ.get("PYTHON3", "python3")


def run(script, *args, **kw):
    result = subprocess.check_output(["/bin/bash", "-c", script],
            stderr=subprocess.STDOUT).decode("utf-8")
    for arg in args:
        assert arg in result, (arg, result)


def test_tar2tsv():
    run(f"{PYTHON3} ./tar2tsv --help",
        "Extract textual")


def test_tarcats():
    run(f"{PYTHON3} ./tarcats --help",
        "Concatenate")


def test_tarfirst():
    run(f"{PYTHON3} ./tarfirst --help",
        "Dump the")


def test_tarmix():
    run(f"{PYTHON3} ./tarmix --help",
        "specified by a YAML")


def test_tarproc():
    run(f"{PYTHON3} ./tarproc --help",
        "Each sample is extracted")


def test_tarshow():
    run(f"{PYTHON3} ./tarshow --help",
        "Show data inside")


def test_tarshow2():
    run(f"{PYTHON3} ./tarshow testdata/imagenet-000000.tar",
        "b'746'",
        "n07734744")


def test_tarsort():
    run(f"{PYTHON3} ./tarsort --help",
        "Sort the samples inside")


def test_tarsplit():
    run(f"{PYTHON3} ./tarsplit --help",
        "Split a tar")


def test_tsv2tar():
    run(f"{PYTHON3} ./tsv2tar --help",
        "Create a tar file")
