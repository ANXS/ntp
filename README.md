## Ansibles - timezone [![Build Status](https://travis-ci.org/Ansibles/timezone.png)](https://travis-ci.org/Ansibles/timezone)

Ansible role which installs and configures ntp.


#### Requirements & Dependencies
- Tested on Ansible 1.4 or higher.


#### Variables

```yaml
ntp_driftfile: "/var/lib/ntp/ntp.drift"
ntp_statsdir: "/var/log/ntpstats/"
ntp_leapfile: "/etc/ntp.leapseconds"
ntp_servers: ["0.pool.ntp.org", "1.pool.ntp.org", "2.pool.ntp.org", "3.pool.ntp.org"]

ntp_restricts:
  - "restrict 0.pool.ntp.org nomodify notrap noquery"
  - "restrict 1.pool.ntp.org nomodify notrap noquery"
  - "restrict 2.pool.ntp.org nomodify notrap noquery"
  - "restrict 3.pool.ntp.org nomodify notrap noquery"
  - "restrict default kod notrap nomodify nopeer noquery"
  - "restrict 127.0.0.1 nomodify"
  - "restrict -6 default kod notrap nomodify nopeer noquery"
  - "restrict -6 ::1 nomodify"
```


#### License

Licensed under the MIT License. See the LICENSE file for details.


#### Feedback, bug-reports, requests, ...

Are [welcome](https://github.com/ansibles/ntp/issues)!
