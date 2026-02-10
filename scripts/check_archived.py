#!/bin/python
import os
import re
import requests

GHRE = re.compile(r'\(https://github.com/(.*?)\)')

token = os.environ["GITHUB_TOKEN"]
headers= {"Authorization": f"Bearer {token}"}

with open('README.md', 'r') as fh:
    for line in fh.readlines():
        if m := GHRE.search(line):
            repo = m.group(1)
            if repo.count('/') != 1:
                # Not a project, probably a deeper path
                continue
            apiurl = f'https://api.github.com/repos/{repo}'
            try:
                r = requests.get(apiurl, headers=headers)
                r.raise_for_status()
                data = r.json()
                if data['archived']:
                    print(f'{repo} is archived\n{line}\n')
            except Exception as e:
                print(f'https://github.com/{repo}: failed to retrieve status: {e}\n')

