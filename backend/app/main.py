# ==========================================
# Project : Jarvis AI Assistant
# File    : main.py
# Purpose : Start the FastAPI server
# Author  : Khushi
# ==========================================

# Import the FastAPI class from the fastapi library.
from fastapi import FastAPI

# Create a FastAPI application object.
app = FastAPI()

# Create our first API (Home Route)
@app.get("/")
def home():
    """
    This function runs when someone opens:
    http://127.0.0.1:8000/
    """
    
    # Return data in JSON format.
    return {
        "message": "Welcome to Jarvis AI Assistant!"
    }



# Create the About API
@app.get("/about")
def about():
    """
    This API returns information about our project.
    """

    return {
        "project": "Jarvis AI Assistant",
        "developer": "Khushi",
        "version": "1.0"
    }



# Create a Greeting API
@app.get("/hello/{name}")
def say_hello(name: str):
    """
    This API greets the user by name.
    """

    return {
        "message": f"Hello {name}, Welcome to Jarvis AI Assistant!"
    }


# Health Check API
@app.get("/health")
def health():
    """
    Check whether the server is running properly.
    """

    return {
        "status": "OK",
        "server": "Running"
    }


# Jarvis Version API
@app.get("/version")
def version():
    """
    Show current Jarvis version.
    """

    return {
        "version": "1.0.0"
    }