#!/bin/sh
cd ~/Desktop/programming/cym/
# If there's a change to index.html
if ! git diff-index --quiet HEAD -- index.html; then
    # Push any changes in index.html to github
    git add index.html
    git commit --quiet -m 'auto cym update'
    git push --quiet
    /usr/local/bin/terminal-notifier -title 'cym' -message 'Automatically updated'  -open 'http://lukasschwab.github.io/cym' -sound default
fi
