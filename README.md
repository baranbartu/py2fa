# py2fa - Basic Command Line OTP Manager

This small life-hack won't save your life, but will definetely prevent possible frustration when you are in the middle of some important thing and your one of the accounts asks the re-auth.

> It is really much more useful when you already use a password manager in parallel, mine is [bitwarden](https://bitwarden.com/)

- You can use already scanned and active barcodes - go to your 2fa app and get the barcode for the related service
- Or, you can generate new barcode via related service.

## Installation
- Directly via setup.py

```
git clone git@github.com:baranbartu/py2fa.git
cd py2fa
python setup.py install

```
- from PYPI - not ready yet

```
pip install py2fa
```

## Environment
This repo implemented in a very short time of period, so tested only on below environment so far. 

- Mac OS (10.15.7)
- Python (3.7.7)

I tried to implement it considering backward-compatibiliy for the python 2.7.*, but you should give it a try and see what happens.

## Security
- There is no remote storage for the `barcodes`
- Barcodes will be stored in `system keyring service (MacOS - keychain)`.
  [keyring](https://github.com/jaraco/keyring) is used to manage it.
- [pyotp](https://github.com/pyauth/pyotp) is used to generate OTP.

## Examples
- To add/update a barcode

```
➜  ~ py2fa add_barcode google barcodeblabla
A barcode with the name `google` is added.

➜  ~ py2fa add_barcode google barcodeblabla
A barcode with the name `google` is updated.
```

- To generate a OTP

```
➜  ~ py2fa otp google
OTP[google]: 344462 - Copied to the clipboard.

➜  ~ py2fa otp notexists
Error - There is no barcode found for this service: notexists
```
