Run a Nagios passive check and submit its result via the Nagios CGI. Use with
`cron`.

Example:

    run-nagios-passive-check-and-submit myhost "My fancy service" /usr/lib/nagios/plugins/check_dummy 1

Requires Python >= 2.7

[![Build Status](https://travis-ci.org/neingeist/run-nagios-passive-check-and-submit.svg?branch=master)](https://travis-ci.org/neingeist/run-nagios-passive-check-and-submit)

Configuration
-------------
You need credentials for the Nagios web interface to submit the check results
via the Nagios CGI. Put those in a configuration file:

`~/.config/run-nagios-passive-check-and-submit.yaml`:
```
---
nagios_url:  https://nagios.example.com/cgi-bin/nagios3/cmd.cgi
nagios_user: myuser
nagios_pass: VeRySeCuRe
ca_bundle:   /etc/ssl/certs/ca-bundle.crt
```
