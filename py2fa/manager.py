import keyring
import pyotp


ACCOUNT = 'py2fa'
SUFFIX = 'barcode'


def add_barcode(service, barcode):
    keychain_name = generate_keychain_name(service)
    old_barcode = keyring.get_password(keychain_name, ACCOUNT)
    created = old_barcode is None
    keyring.set_password(keychain_name, ACCOUNT, barcode)
    return created


def generate_otp(service):
    keychain_name = generate_keychain_name(service)
    barcode = keyring.get_password(keychain_name, ACCOUNT)
    if barcode is None:
        raise ValueError('There is no barcode found for this service: {}'.format(service))

    totp = pyotp.TOTP(barcode)
    return totp.now()


def generate_keychain_name(service):
    return '{service}-{suffix}'.format(service=service, suffix=SUFFIX)
