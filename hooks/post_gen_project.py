#!/usr/bin/python
# -*- coding: utf-8 -*-

import os

PROJECT_ROOT = os.path.realpath(os.path.curdir)

# cat post_gen_project.py
import os
import shutil

print(os.getcwd())  # prints /absolute/path/to/
print(PROJECT_ROOT)  # prints /absolute/path/to/

def remove(filepath):
    print("Removing: " + filepath)
    if os.path.isfile(filepath):
        os.remove(filepath)
    elif os.path.isdir(filepath):
        shutil.rmtree(filepath)

use_jmh = '{{cookiecutter.use_jmh}}' == 'y'
use_coroutines = '{{cookiecutter.use_coroutines}}' == 'y'
use_native_builder = '{{cookiecutter.use_native_builder}}' == 'y'

if not use_jmh:
    # remove top-level file inside the generated folder
    remove(os.path.join(PROJECT_ROOT, 'src', 'jmh'))

if not use_native_builder:
    remove(os.path.join(PROJECT_ROOT, 'graal-reflection.json'))

print(" I am initializing gggg....................")