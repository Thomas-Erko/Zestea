import os
import subprocess
from subprocess import Popen
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, render_template, request, url_for, redirect, session
from progress.Python.option1 import *


def loader(running):
    while True:
        poll = running.poll()
        if poll is not None:
            False

    return True


def prefetch(x):
    commands = ['bash', 'progress/Bash/Start.sh', x]
    script = subprocess.Popen(commands)
    return script 

def topleft(pagename):
    if "sin" not in session:
        return render_template(pagename, logsin = '<li><a href="login">Log In</a></li>' )
    elif "sin" in session:
        return render_template(pagename, logsin = '<li><a href="account">Account</a></li>' )