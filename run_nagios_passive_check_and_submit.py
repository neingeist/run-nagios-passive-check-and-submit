#!/usr/bin/python
"""
Run a Nagios passive check and submit its result via the CGI interface
"""

from __future__ import division, print_function
from termcolor import colored
import os.path
import requests
import subprocess
import sys
import yaml


def run_check(check):
    try:
        plugin_output = subprocess.check_output(check)
        plugin_state = 0
    except subprocess.CalledProcessError as e:
        plugin_output = e.output
        plugin_state = e.returncode
    plugin_output = plugin_output.strip()
    plugin_output = plugin_output.splitlines()[0]

    return plugin_state, plugin_output


def submit_result(host, service, plugin_state, plugin_output):
    config_filename = '~/.config/run-nagios-passive-check-and-submit.yaml'
    config = yaml.load(open(os.path.expanduser(config_filename)))

    payload = {
        'cmd_typ': 30,
        'cmd_mod': 2,
        'host': host,
        'service': service,
        'plugin_state': plugin_state,
        'plugin_output': plugin_output,
        'btnSubmit': 'Commit'
    }

    r = requests.get(config['nagios_url'], params=payload,
                     auth=(config['nagios_user'], config['nagios_pass']),
                     verify=config['ca_bundle'])
    return r.status_code


def main():
    host = sys.argv[1]
    service = sys.argv[2]
    check = sys.argv[3:]
    plugin_state, plugin_output = run_check(check)

    status_code = submit_result(host, service, plugin_state, plugin_output)

    if status_code != 200:
        print(colored('HTTP status code {} while submitting check result:'
                      .format(status_code), 'red'))
    if plugin_state in [0, 1, 2, 3]:
        colors = ['green', 'yellow', 'red', 'orange']
        print(colored('[{}] {}'.format(plugin_state, plugin_output),
                      colors[plugin_state]))
    else:
        print(colored('Called plugin failed with return code {}'
                      .format(plugin_state), 'orange'))
        sys.exit(3)


if __name__ == '__main__':
    main()
