#! /usr/bin/env bash
TLDEXTRACT_CACHE="."

# get
python3 get_blacklists.py
python3 get_top_1000000.py

# commit
git add blacklist.txt
git commit -m "automatic blacklist update"

git add top_1000000.txt
git commit -m "automatic top 1M update"

# push
git push
