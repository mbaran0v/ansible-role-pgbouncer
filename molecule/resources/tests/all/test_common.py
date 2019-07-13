debian_os = ['debian', 'ubuntu']
rhel_os = ['redhat', 'centos']


def test_distribution(host):
    assert host.system_info.distribution.lower() in debian_os + rhel_os


def test_conf_dir(host):
    f = host.file('/etc/pgbouncer')

    assert f.exists
    assert f.is_directory


def test_log_dir(host):
    f = host.file('/var/log/pgbouncer')

    assert f.exists
    assert f.is_directory


def test_service(host):
    s = host.service('pgbouncer')

    assert s.is_enabled
    assert s.is_running


def test_socket(host):
    s = host.socket("tcp://127.0.0.1:6432")

    assert s.is_listening
