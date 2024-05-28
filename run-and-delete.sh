#!/bin/bash

# Update the package list and install necessary packages
apk update
apk add python3
apk add py3-pip
apk add vim
apk add ffmpeg

# Check disk space
echo "Checking disk space..."
df -h | grep '/dev/loop'

# Create and activate the virtual environment
echo "Creating and activating virtual environment..."
python3 -m venv .venv
source .venv/bin/activate

# Install necessary Python packages
echo "Installing Python packages..."
python3 -m pip install requests
python3 -m pip install python-dotenv
python3 -m pip install -U streamlink

# Set the default editor to vim
export EDITOR=vim

# Deactivate the virtual environment
deactivate

# Create the svod directory and navigate into it
mkdir -p svod
cd svod

# Get user input for the .env file
echo "Creating .env file..."
read -p "Enter botChannelID: " DCCID
read -p "Enter userID: " DCUID
read -p "Enter userToken: " DCT

# Write the .env file
cat <<EOL > .env
DCCID=$DCCID
DCUID=$DCUID
DCT=$DCT
EOL

# Check if the .env file is created
echo ".env file created with the following content:"
cat .env

# Download jive.py
echo "Downloading jive.py..."
wget -O jive.py https://raw.githubusercontent.com/cltWilly/alpine-scripts/main/sendSlashCommand2Bot.py

# Download keep.sh and make it executable
echo "Downloading keep.sh..."
wget -O keep.sh https://raw.githubusercontent.com/cltWilly/alpine-scripts/main/keep.sh
chmod +x keep.sh

# Test keep.sh
echo "Testing keep.sh..."
bash keep.sh

# Setup crontab
echo "Setting up crontab..."
(crontab -l ; echo "0 0 */4 * * bash /root/svod/keep.sh") | crontab -

echo "Setup complete."
