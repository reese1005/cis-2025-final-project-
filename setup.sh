#!/bin/bash

# Initialize the repository and set up the remote
echo "# cis-2023-final-project-" >> README.md

# Initialize Git repository
git init

# Add README.md to the repository
git add README.md

# Commit the README file with a message
git commit -m "first commit"

# Rename the default branch to main
git branch -M main

# Add the remote repository (replace with your actual GitHub repository link)
git remote add origin https://github.com/reese1005/cis-2023-final-project-.git

# Push the changes to GitHub
git push -u origin main
