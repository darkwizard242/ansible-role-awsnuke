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


def test_awsnuke_configdir_isdirectory(host):
    assert host.file('/etc/aws-nuke').is_directory


def test_awsnuke_configdir_ownedbyuser(host):
    assert host.file('/etc/aws-nuke').user == 'root'


def test_awsnuke_configdir_ownedbygroup(host):
    assert host.file('/etc/aws-nuke').group == 'root'


def test_awsnuke_configfile_exists(host):
    assert host.file('/etc/aws-nuke/aws-nuke-config.yml').exists


def test_awsnuke_configfile_ownedbyuser(host):
    assert host.file('/etc/aws-nuke/aws-nuke-config.yml').user == 'root'


def test_awsnuke_configfile_ownedbygroup(host):
    assert host.file('/etc/aws-nuke/aws-nuke-config.yml').group == 'root'
