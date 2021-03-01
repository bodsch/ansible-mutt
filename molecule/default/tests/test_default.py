
from ansible.parsing.dataloader import DataLoader
from ansible.template import Templar
import pytest
import os
import testinfra.utils.ansible_runner

import pprint
pp = pprint.PrettyPrinter()

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def base_directory():
    cwd = os.getcwd()
    pp.pprint(cwd)
    pp.pprint(os.listdir(cwd))

    if('group_vars' in os.listdir(cwd)):
        directory = "../.."
        molecule_directory = "."
    else:
        directory = "."
        molecule_directory = "molecule/{}".format(os.environ.get('MOLECULE_SCENARIO_NAME'))

    return directory, molecule_directory


@pytest.fixture()
def get_vars(host):
    """

    """
    base_dir, molecule_dir = base_directory()

    pp.pprint(" => '{}' / '{}'".format(base_dir, molecule_dir))

    file_defaults = "file={}/defaults/main.yml name=role_defaults".format(base_dir)
    file_vars = "file={}/vars/main.yml name=role_vars".format(base_dir)
    file_molecule = "file={}/group_vars/all/vars.yml name=test_vars".format(molecule_dir)

    defaults_vars = host.ansible("include_vars", file_defaults).get("ansible_facts").get("role_defaults")
    vars_vars = host.ansible("include_vars", file_vars).get("ansible_facts").get("role_vars")
    molecule_vars = host.ansible("include_vars", file_molecule).get("ansible_facts").get("test_vars")

    ansible_vars = defaults_vars
    ansible_vars.update(vars_vars)
    ansible_vars.update(molecule_vars)

    templar = Templar(loader=DataLoader(), variables=ansible_vars)
    result = templar.template(ansible_vars, fail_on_undefined=False)

    return result

@pytest.mark.parametrize("packages", [
    "mutt",
])
def test_packages(host, packages):
    p = host.package(packages)
    assert p.is_installed

@pytest.mark.parametrize("dirs", [
    ".mutt",
    ".mutt/cache",
    ".mutt/messages",
    ".mutt/tmp",
    ".mutt/colors"
])
def test_directories(host, dirs, get_vars):
    h = get_vars.get('mutt_home_dir')

    d = host.file("{home_dir}/{directory}".format(home_dir=h, directory=dirs))
    assert d.is_directory
    assert d.exists


@pytest.mark.parametrize("files", [
    ".muttrc",
    ".mutt/signature",
    ".mutt/aliases",
    ".mutt/colors/mutt-colors-solarized-dark-256.muttrc",
    ".mutt/colors/mutt-colors-solarized-light-256.muttrc",
    ".mutt/colors/mutt-colors-solarized-dark-16.muttrc",
    ".mutt/colors/mutt-colors-solarized-light-16.muttrc",
])
def test_files(host, files, get_vars):
    h = get_vars.get('mutt_home_dir')

    f = host.file("{home_dir}/{filename}".format(home_dir=h, filename=files))
    assert f.exists
    assert f.is_file
