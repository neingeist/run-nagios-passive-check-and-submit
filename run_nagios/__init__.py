from __future__ import division, print_function
from bs4 import BeautifulSoup
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

    # Extract error message if any
    soup = BeautifulSoup(r.content)
    error_div = soup.find('div', attrs={'class': 'errorMessage'})
    if error_div:
        error_text = error_div.text
    else:
        error_text = None

    return (r.status_code, error_text)
