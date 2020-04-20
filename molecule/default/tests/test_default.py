import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_awsnuke_binary_exists(host):
    assert host.file('/usr/local/bin/aws-nuke').exists


def test_awsnuke_binary_file(host):
    assert host.file('/usr/local/bin/aws-nuke').is_file


def test_awsnuke_binary_which(host):
    assert host.check_output('which aws-nuke') == '/usr/local/bin/aws-nuke'
