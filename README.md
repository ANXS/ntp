## ANXS - ntp [![Build Status](https://travis-ci.org/ANXS/ntp.png)](https://travis-ci.org/ANXS/ntp)

Ansible role which installs and configures ntp.


#### Requirements & Dependencies
- Tested on Ansible 1.3 or higher.


#### Variables

* `ntp_timezone` defaults to `UTC`
* `ntp_driftfile` defaults to `/var/lib/ntp/ntp.drift`
* `ntp_statsdir` defaults to `/var/log/ntpstats/`
* `ntp_servers` defaults to the following
```yaml
- "0.pool.ntp.org"
- "1.pool.ntp.org"
- "2.pool.ntp.org"
- "3.pool.ntp.org"
```
* `auto_ntpdate` controls whether or not to periodically run `ntpdate`. Helpful with some troublesome virtual machines. It defaults to `no`.
* `auto_ntpdate_hour` determines which hour of the day to periodically run `ntpdate`. Defaults to `12`.
* `ntp_leapfile` defaults to `/etc/ntp.leapseconds`
* `ntp_leapurl` is the URL to retrieve the leap seconds file from. It defaults to `http://www.ietf.org/timezones/data/leap-seconds.list`.
* `ntp_restricts` defaults to the following
```yaml
- "restrict 0.pool.ntp.org nomodify notrap noquery"
- "restrict 1.pool.ntp.org nomodify notrap noquery"
- "restrict 2.pool.ntp.org nomodify notrap noquery"
- "restrict 3.pool.ntp.org nomodify notrap noquery"
- "restrict default kod notrap nomodify nopeer noquery"
- "restrict 127.0.0.1 nomodify"
- "restrict -6 default kod notrap nomodify nopeer noquery"
- "restrict -6 ::1 nomodify"
```

#### Testing
This project comes with a VagrantFile, this is a fast and easy way to test changes to the role, fire it up with `vagrant up`

See [vagrant docs](https://docs.vagrantup.com/v2/) for getting setup with vagrant


#### License

Licensed under the MIT License. See the LICENSE file for details.


#### Feedback, bug-reports, requests, ...

Are [welcome](https://github.com/ANXS/ntp/issues)!
