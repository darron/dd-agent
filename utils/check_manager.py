# stdlib
import os

# 3p
import requests

# project

OFFICIAL_REPOSITORY = 'https://raw.githubusercontent.com/tmichelet/dd-checks/master/checks.json'
CHECKS_PATH = 'checks.e'
CONF_PATH = 'conf.e'

class CheckNotFound(Exception):
    pass


class CheckManager(object):
    """
    Compress all important logs and configuration files for debug,
    and then send them to Datadog (which transfers them to Support)
    """
    pass

    @classmethod
    def install(cls, check_name, *args, **kwargs):
        checks_list = requests.get(OFFICIAL_REPOSITORY).json()
        if check_name not in checks_list:
            raise CheckNotFound()

        check_repository = checks_list[check_name]

        files_to_download = {
            CHECKS_PATH: 'check.py',
            CONF_PATH: 'check.yaml.example',
        }

        for directory, filename in files_to_download.iteritems():
            file_url = '%s/master/%s' % (check_repository, filename)
            file_path = os.path.join(directory, filename.replace('check', check_name))
            r = requests.get(file_url)
            with open(file_path, 'w') as _file:
                _file.write(r.content)

        return 1
