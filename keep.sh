#!/bin/bash

# Create the virtual environment if it does not exist
if [ ! -d ".venv" ]; then
    echo "Virtual environment '.venv' does not exist. Creating it now..."
    python3 -m venv .venv
    if [ $? -ne 0 ]; then
        echo "Failed to create virtual environment '.venv'."
        exit 1
    fi
    echo "Virtual environment '.venv' created."
fi

# Activate the virtual environment
source .venv/bin/activate

# Check if activation was successful
if [[ "$VIRTUAL_ENV" != "" ]]; then
    echo "Virtual environment '.venv' activated."
else
    echo "Failed to activate virtual environment '.venv'."
    exit 1
fi

# Run the Python script
python3 /root/svod/jive.py

# Deactivate the virtual environment
deactivate

# Confirm deactivation
if [[ "$VIRTUAL_ENV" == "" ]]; then
    echo "Virtual environment '.venv' deactivated."
else
    echo "Failed to deactivate virtual environment '.venv'."
fi
