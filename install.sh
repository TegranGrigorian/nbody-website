#!/bin/bash

sudo apt update
sudo apt install -y python3-virtualenv

cd nbody-website
if [ -d ".venv" ]; then
    rm -rf .venv
fi

virtualenv .venv --python=python3

source .venv/bin/activate
pip install -r requirements.txt