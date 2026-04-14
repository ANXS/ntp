## [ANXS](https://github.com/ANXS) - ntp

[![CI Status](https://img.shields.io/github/actions/workflow/status/anxs/ntp/ci.yml)](https://github.com/ANXS/ntp/actions/workflows/ci.yml)
[![Maintenance](https://img.shields.io/maintenance/yes/2026.svg)](https://github.com/ANXS/ntp)
[![Ansible Role](https://img.shields.io/ansible/role/d/anxs/ntp)](https://galaxy.ansible.com/ui/standalone/roles/ANXS/ntp/)
[![License](https://img.shields.io/github/license/ANXS/ntp)](https://github.com/ANXS/ntp/blob/master/LICENSE)

Ansible role for installing and configuring NTP time synchronization. Manages the NTP daemon, server/pool configuration, access restrictions, leap seconds file, and optional periodic ntpdate sync via cron or systemd timer. Supports both classic ntp and ntpsec (Debian 13+).

## Requirements & Dependencies

* Ansible 2.12 or higher.
* Ubuntu 20.04+ or Debian 11+.

## Variables

A partial listing of high-impact variables. See `defaults/main.yml` for the full set.

* `ntp_servers` (defaults to `0-3.pool.ntp.org`) controls the list of NTP servers to sync against.
* `ntp_auto_update` (defaults to `false`) enable periodic ntpdate sync as a forcing function.
  * `ntp_use_systemd_timer` (defaults to `false` unless on Ubuntu noble) use a systemd timer instead of cron.
  * `ntp_auto_update_hour` (defaults to `12`) to change the hour interval for periodic sync.
* `ntp_timezone` (defaults to `UTC`) for the system timezone.

## Testing

Tests use [Molecule](https://github.com/ansible/molecule) with Docker and [Testinfra](https://testinfra.readthedocs.io/). Run the full suite with `make test`, or target a specific platform (e.g. `make test-ubuntu2404`).

The test suite verifies package installation (ntp/ntpsec), config file permissions, server and restriction directives, driftfile presence, leap seconds file fetch, and NTP service status. Tests run across all supported Linux distributions.

## Note on AI Usage

This project has been developed with AI assistance. Contributions making use of AI generated content are welcome, however they _must_ be human reviewed prior to submission as pull requests, or issues. All contributors must be able to fully explain and defend any AI generated code, documentation, issues, or tests they submit. Contributions making use of AI must have this explicitly declared in the pull request or issue. This also applies to utilization of AI for reviewing of pull requests.

## Feedback, bug-reports, requests, ...

Are always [welcome](https://github.com/ANXS/ntp/issues)!
