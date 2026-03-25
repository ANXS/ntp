"""Testinfra tests for anxs-ntp role."""


def test_ntp_package_installed(host):
    """Verify NTP package is installed."""
    # Debian 13+ uses ntpsec, others use ntp
    ntp = host.package("ntpsec")
    if not ntp.is_installed:
        ntp = host.package("ntp")
    assert ntp.is_installed


def test_ntpdate_package_installed(host):
    """Verify ntpdate package is installed."""
    ntpdate = host.package("ntpsec-ntpdate")
    if not ntpdate.is_installed:
        ntpdate = host.package("ntpdate")
    assert ntpdate.is_installed


def test_ntp_config_exists(host):
    """Verify ntp.conf exists with correct permissions."""
    f = host.file("/etc/ntp.conf")
    assert f.exists
    assert f.is_file
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o660


def test_ntp_config_has_servers(host):
    """Verify ntp.conf contains server definitions."""
    f = host.file("/etc/ntp.conf")
    content = f.content_string
    assert "pool.ntp.org" in content


def test_ntp_config_has_driftfile(host):
    """Verify ntp.conf contains driftfile directive."""
    f = host.file("/etc/ntp.conf")
    content = f.content_string
    assert "driftfile" in content


def test_ntp_config_has_restrictions(host):
    """Verify ntp.conf contains restrict directives."""
    f = host.file("/etc/ntp.conf")
    content = f.content_string
    assert "restrict" in content
    assert "nomodify" in content


def test_leapseconds_file_exists(host):
    """Verify leap seconds file was fetched."""
    f = host.file("/etc/ntp.leapseconds")
    assert f.exists
    assert f.is_file
    assert f.mode == 0o660


def test_ntp_service_running(host):
    """Verify NTP service is running."""
    # Try ntpsec first (Debian 13+), then ntp
    svc = host.service("ntpsec")
    if not svc.is_running:
        svc = host.service("ntp")
    assert svc.is_running
    assert svc.is_enabled
