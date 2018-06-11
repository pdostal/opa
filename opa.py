#!/usr/bin/env python3

import requests
import click
import re

@click.command()
@click.argument('url', nargs=1)

def prepare_url(url):
    """Validate and prepare the URL of the test"""
    parsed = re.search(r'(http[s]*://.*)/tests/([0-9]*)[#|/]*.*', url)
    if parsed:
      click.echo('Detected test %s on %s instance' % (parsed.group(2), parsed.group(1)) )
      return parsed.group(1)+'/tests/'+parsed.group(2)
    else:
      click.echo('The URL cannot be detected!')
      exit(1)

if __name__ == '__main__':
    prepare_url()

