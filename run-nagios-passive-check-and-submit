#!/usr/bin/python
"""
Run a Nagios passive check and submit its result via the CGI interface
"""

from __future__ import division, print_function
import requests
import sys
import termcolor

from run_nagios import run_check, submit_result


def colored(*args, **kwargs):
    if sys.stdout.isatty():
        return termcolor.colored(*args, **kwargs)
    else:
        return args[0]


def main():
    if sys.argv[1] == "--host":
        host = sys.argv[2]
        service = None
        check = sys.argv[3:]
    else:
        host = sys.argv[1]
        service = sys.argv[2]
        check = sys.argv[3:]
    plugin_state, plugin_output = run_check(check)
    plugin_output = plugin_output.decode('utf-8')

    if plugin_state in [0, 1, 2, 3]:
        colors = ['green', 'yellow', 'red', 'yellow']
        print(colored('[{}] {}'.format(plugin_state, plugin_output),
                      colors[plugin_state]))
    else:
        print(colored('Called plugin failed with return code {}'
                      .format(plugin_state), 'yellow'))
        sys.exit(3)

    try:
        status_code, error_text = submit_result(host, service,
                                                plugin_state, plugin_output)

        if status_code != 200:
            print(colored('HTTP status code {} while submitting check result:'
                          .format(status_code), 'red'))

        if error_text:
            print(colored('Nagios error: {}'.format(error_text), 'red'))

    except requests.exceptions.ConnectionError as e:
        try:
            print(colored('Connection error while submitting check result: {}'
                  .format(e), 'red'))
        except TypeError as e:
            if '__str__ returned non-string' in str(e):
                print(colored('urllib3 had an SSL handshake error with'
                              'pyOpenSSL', 'red'))
            else:
                raise e


if __name__ == '__main__':
    main()
