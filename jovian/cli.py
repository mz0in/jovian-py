import argparse
import webbrowser
from jovian.utils.clone import clone, pull
from jovian.utils.install import install, activate
from jovian._version import __version__


def exec_clone(slug, version):
    clone(slug, version)


def exec_init():
    from jovian.utils.api import get_api_key
    from jovian.utils.credentials import get_guest_key
    # webbrowser.open('https://jvn.io/')
    get_guest_key()
    get_api_key()
    print('Initialization finished')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command')
    parser.add_argument('gist', nargs='?')
    parser.add_argument('-n', '--name')
    parser.add_argument('-v', '--version')

    args = parser.parse_args()
    command = args.command
    if command == 'init':
        exec_init()
    elif command == 'clone':
        if not args.gist:
            print('Please provide the Gist ID to clone')
            return
        exec_clone(args.gist, args.version)
    elif command == 'pull':
        pull(args.gist, args.version)
    elif command == 'version':
        print('Jovian library version: ' + __version__)
    elif command == 'install':
        install(env_name=args.name)
    elif command == 'activate':
        activate()


if __name__ == '__main__':
    main()
