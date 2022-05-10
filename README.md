[![build-test](https://github.com/darkwizard242/ansible-role-awsnuke/workflows/build-and-test/badge.svg?branch=master)](https://github.com/darkwizard242/ansible-role-awsnuke/actions?query=workflow%3Abuild-and-test) [![release](https://github.com/darkwizard242/ansible-role-awsnuke/workflows/release/badge.svg)](https://github.com/darkwizard242/ansible-role-awsnuke/actions?query=workflow%3Arelease) ![Ansible Role](https://img.shields.io/ansible/role/48139?color=dark%20green%20) ![Ansible Role](https://img.shields.io/ansible/role/d/48139?label=role%20downloads) ![Ansible Quality Score](https://img.shields.io/ansible/quality/48139?label=ansible%20quality%20score) [![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-awsnuke&metric=alert_status)](https://sonarcloud.io/dashboard?id=ansible-role-awsnuke) [![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-awsnuke&metric=sqale_rating)](https://sonarcloud.io/dashboard?id=ansible-role-awsnuke) [![Reliability Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-awsnuke&metric=reliability_rating)](https://sonarcloud.io/dashboard?id=ansible-role-awsnuke) [![Security Rating](https://sonarcloud.io/api/project_badges/measure?project=ansible-role-awsnuke&metric=security_rating)](https://sonarcloud.io/dashboard?id=ansible-role-awsnuke) ![GitHub tag (latest SemVer)](https://img.shields.io/github/tag/darkwizard242/ansible-role-awsnuke?label=release) ![GitHub repo size](https://img.shields.io/github/repo-size/darkwizard242/ansible-role-awsnuke?color=orange&style=flat-square)

# Ansible Role: awsnuke

Role to install (_by default_) [aws-nuke](https://github.com/rebuy-de/aws-nuke) on **Debian/Ubuntu** and **EL** systems.

## Requirements

None.

## Role Variables

Available variables are listed below (located in `defaults/main.yml`):

### Variables list:

```yaml
awsnuke_app: aws-nuke
awsnuke_version: 2.18.1
awsnuke_os: linux
awsnuke_arch: amd64
awsnuke_dl_url: https://github.com/rebuy-de/{{ awsnuke_app }}/releases/download/v{{ awsnuke_version }}/{{ awsnuke_app }}-v{{ awsnuke_version }}-{{ awsnuke_os }}-{{ awsnuke_arch }}.tar.gz
awsnuke_app_owner: root
awsnuke_app_group: root
awsnuke_bin_path: /usr/local/bin
awsnuke_file_mode: '0755'
awsnuke_config_dir: "/etc/{{ awsnuke_app }}"
awsnuke_config_dir_mode: '0744'
awsnuke_config_dir_owner: root
awsnuke_config_dir_group: root
awsnuke_template_source: aws-nuke-config.yml.j2
awsnuke_template_dest: aws-nuke-config.yml
awsnuke_template_dest_mode: '0744'
awsnuke_template_dest_owner: root
awsnuke_template_dest_group: root
```

### Variables table:

Variable                    | Description
--------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------
awsnuke_app                 | Defines the app to install i.e. **aws-nuke**
awsnuke_version             | Defined to dynamically fetch the desired version to install. Defaults to: **2.18.1**
awsvault_os                 | Defines os type. Used for obtaining the correct type of binaries based on OS type. Defaults to: **linux**
awsvault_arch               | Defines os architecture. Used to set the correct type of binaries based on OS System Architecture. Defaults to: **amd64**
awsnuke_dl_url              | Defines URL to download the awsnuke binary from.
awsnuke_config_dir_owner    | Owner of aws-nuke binary file.
awsnuke_config_dir_group    | Group of aws-nuke binary file.
awsnuke_bin_path            | Defined to dynamically set the appropriate path to store awsnuke binary into. Defaults to (as generally available on any user's PATH): **/usr/local/bin**
awsnuke_file_mode           | Mode for the binary file of aws-nuke.
awsnuke_config_dir          | Defined to create directory to store aws-nuke config file in.
awsnuke_config_dir_mode     | Permissions for aws-nuke config directory.
awsnuke_config_dir_owner    | Owner of aws-nuke config directory.
awsnuke_config_dir_group    | Group of aws-nuke config directory.
awsnuke_template_source     | Source config template file to utilize.
awsnuke_template_dest       | Filename as to be placed in the configuration directory as for aws-nuke.
awsnuke_template_dest_mode  | Permission of aws-nuke configuration file.
awsnuke_template_dest_owner | Owner of aws-nuke configuration file.
awsnuke_template_dest_group | Group of aws-nuke configuration file.

## Dependencies

None

## Example Playbook

For default behaviour of role (i.e. installation of **awsnuke**) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.awsnuke
```

For customizing behavior of role (i.e. specifying the desired **awsnuke** version) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.awsnuke
  vars:
    awsnuke_version: 2.13.0
```

For customizing behavior of role (i.e. placing binary of **awsnuke** package in different location) in ansible playbooks.

```yaml
- hosts: servers
  roles:
    - darkwizard242.awsnuke
  vars:
    awsnuke_bin_path: /bin/
```

## License

[MIT](https://github.com/darkwizard242/ansible-role-awsnuke/blob/master/LICENSE)

## Author Information

This role was created by [Ali Muhammad](https://www.linkedin.com/in/ali-muhammad-759791130/).
