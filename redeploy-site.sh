#!/bin/bash
tmux kill-server
cd week1-pe-portfolio-site/
git fetch && git reset origin/main --hard
source python3-virtualenv/bin/activate
pip install -r requirements.txt
tmux new-session -d -s "newsession"
tmux send-keys -t "newsession" "flask run --host=0.0.0.0" Enter
