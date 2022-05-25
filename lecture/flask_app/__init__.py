from flask import Flask, redirect, render_template, request, session
from users import User
app = Flask(__name__)

app.secret_key = "Justw0rk!"