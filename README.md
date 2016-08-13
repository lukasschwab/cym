# cym
<p align="center">
cym is like <a href="https://github.com/lukasschwab/tir">tir</a>, but for what you're listening to.<br>
Right now it's very WIP.<br><br>
<img src="http://lukasschwab.github.io/img/cym.gif">
</p>

***

## Setup

1. Download/unzip or clone this repository: `git clone https://github.com/lukasschwab/cym.git`.

2. Optionally, move `index.html` to a desired location (e.g. if you don't want to host cym separately, move `index.html` into a GitHub Pages repo). Simplest setup with GitHub Pages would be to create a gh-pages branch (`git branch gh-pages`) and leave `index.html` where it is.

3. Modify [cym/\_\_main\_\_.py](https://github.com/lukasschwab/cym/blob/master/cym/__main__.py) so that the path on line four points to your local copy of `index.html`. For example, `html = "~/Desktop/index/index.html"`.

4. *After changing that path*, run `python setup.py install` from the project root directory.

5. From the command line, just run `cym`.

## To do

+ Add nonchalant link from blog

+ Some description text on the page itself

+ Store list of past videos––can reuse a tir table construction structure, but just with links and dates.

+ Fix fullscreen mode

+ Taylor says the layout is bad on mobile; check this and fix any apparent issues.

+ RSS (via tir work? Can use same plugin with same list generator?)