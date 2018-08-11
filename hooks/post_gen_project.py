#!/usr/bin/env python3

import os
import shutil

PROJECT_ROOT = os.path.realpath(os.path.curdir)


def remove(filepath):
    print("Removing: " + filepath)
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)

use_jmh = '{{cookiecutter.use_jmh}}' == 'y'
use_native_builder = '{{cookiecutter.use_native_builder}}' == 'y'

if not use_jmh:
    # remove top-level file inside the generated folder
    remove(os.path.join(PROJECT_ROOT, 'src', 'jmh'))

if not use_native_builder:
    remove(os.path.join(PROJECT_ROOT, 'graal-reflection.json'))