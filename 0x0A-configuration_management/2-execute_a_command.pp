# Define a Puppet manifest to kill a process named "killmenow"
exec { 'pkill -f killmenow':
  path        => '/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin',
}