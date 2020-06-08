# coding: utf-8
from __future__ import unicode_literals

import pytest
import re
import os
import yaml
import json

# import testinfra
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


@pytest.fixture()
def get_vars(host):
    defaults_files = "file=../../defaults/main.yml name=role_defaults"
    vars_files = "file=../../vars/main.yml name=role_vars"

    ansible_vars = host.ansible(
        "include_vars",
        defaults_files)["ansible_facts"]["role_defaults"]

    ansible_vars.update(host.ansible(
        "include_vars",
        vars_files)["ansible_facts"]["role_vars"])

    print(ansible_vars)

    return ansible_vars


@pytest.mark.parametrize("dirs", [
    ".mutt",
    ".mutt/cache",
    ".mutt/messages",
    ".mutt/tmp",
])
def test_directories(host, dirs, get_vars):
    h = get_vars['mutt_home_dir']
    d = host.file("{}/{}".format(h,dirs))
    assert d.is_directory
    assert d.exists


@pytest.mark.parametrize("files", [
    ".muttrc",
    ".mutt/signature",
    ".mutt/aliases",
    ".mutt/mutt-colors-solarized-dark-256.muttrc",
])
def test_files(host, files, get_vars):
    h = get_vars['mutt_home_dir']
    f = host.file("{}/{}".format(h,files))
    assert f.exists
    assert f.is_file
