import os

def run(**args):
    print("[*] In dirlster module.")
    files = os.listdir(".")
    return str(files)
