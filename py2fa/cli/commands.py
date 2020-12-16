import pyperclip

from py2fa.cli.builder import command, argument, Command
from py2fa import manager


@command
@argument('service')
@argument('barcode')
def add_barcode(args):
    service = args.service
    barcode = args.barcode

    created = manager.add_barcode(service, barcode)

    action = 'added' if created else 'updated'
    msg = 'A barcode with the name `{service}` is {action}.'.format(service=service, action=action)
    print(msg)


@command
@argument('service')
def otp(args):
    service = args.service
    otp = manager.generate_otp(service)
    pyperclip.copy(otp)
    msg = 'OTP[{service}]: {otp} - Copied to the clipboard.'.format(service=service, otp=otp)
    print(msg)


def load_commands():
    import py2fa.cli.commands as commands

    attrs = set(dir(commands))
    return filter(lambda f: isinstance(f, Command),
                  map(lambda attr: getattr(commands, attr), attrs))
