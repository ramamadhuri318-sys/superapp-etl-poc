#!/bin/bash
set -e
echo "🚀 Initializing Git repository..."
git init
git add .
git commit -m "Initial commit for superapp-etl-poc"
git branch -M main
git remote add origin https://github.com/Synxa-IT-Pvt-LTD/superapp-etl-poc.git
git push -u origin main
echo "✅ Code successfully pushed to GitHub."
