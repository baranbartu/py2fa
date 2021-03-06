from py2fa.cli.builder import CommandParser
from py2fa.cli.commands import load_commands


def main():
    parser = CommandParser(fromfile_prefix_chars='@')
    for command in load_commands():
        parser.add_command(command)

    parser.run()


if __name__ == "__main__":
    main()
