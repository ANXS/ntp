#!/usr/bin/env bash
set -e
/usr/sbin/service ntp stop
/usr/sbin/ntpdate-debian
/usr/sbin/service ntp start
