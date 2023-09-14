import os

from art import *
from prozac import Prozac

def run():
    startup()
    Prozac().listen()

def startup():
    os.system('color')
    os.system(f"title Prozac")
    print(text2art("Prozac", font="doom"))

run()
