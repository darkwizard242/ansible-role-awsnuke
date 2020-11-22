import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE_BINARY = '/usr/local/bin/aws-nuke'
PACKAGE_CONFIG_DIR = '/etc/aws-nuke'
PACKAGE_CONFIF_FILE = '/etc/aws-nuke/aws-nuke-config.yml'


def test_awsnuke_binary_exists(host):
    """
    Tests if aws-nuke binary exists.
    """
    assert host.file(PACKAGE_BINARY).exists


def test_awsnuke_binary_file(host):
    """
    Tests if aws-nuke binary is a file type.
    """
    assert host.file(PACKAGE_BINARY).is_file


def test_awsnuke_binary_which(host):
    """
    Tests the output to confirm aws-nuke's binary location.
    """
    assert host.check_output('which aws-nuke') == PACKAGE_BINARY


def test_awsnuke_configdir_isdirectory(host):
    """
    Tests if /etc/aws-nuke is a directory.
    """
    assert host.file(PACKAGE_CONFIG_DIR).is_directory


def test_awsnuke_configdir_ownedbyuser(host):
    """
    Tests if /etc/aws-nuke is owned by user root.
    """
    assert host.file(PACKAGE_CONFIG_DIR).user == 'root'


def test_awsnuke_configdir_ownedbygroup(host):
    """
    Tests if /etc/aws-nuke is owned by group root.
    """
    assert host.file(PACKAGE_CONFIG_DIR).group == 'root'


def test_awsnuke_configfile_exists(host):
    """
    Tests if /etc/aws-nuke/aws-nuke-config.yml exists.
    """
    assert host.file(PACKAGE_CONFIF_FILE).exists


def test_awsnuke_configfile_ownedbyuser(host):
    """
    Tests if /etc/aws-nuke/aws-nuke-config.yml is owned by user root.
    """
    assert host.file(PACKAGE_CONFIF_FILE).user == 'root'


def test_awsnuke_configfile_ownedbygroup(host):
    """
    Tests if /etc/aws-nuke/aws-nuke-config.yml is owned by group root.
    """
    assert host.file(PACKAGE_CONFIF_FILE).group == 'root'
