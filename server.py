from flask import Flask, render_template, request, redirect, session
from dojoninja_app import app
from dojoninja_app.controlles import dojos_controller, ninjas_controller


if __name__ == "__main__":
    app.run( debug = True ) #This needs to do at te end of the app so it takes all the commands included above during the debug 