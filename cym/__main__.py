import click, sys, os, webbrowser

# NOTE: change this to your html location
html = "~/Programming/cym/index.html"

# HANDLING FILE

# Read file contents
path = os.path.expanduser(html)
with open(path, "r") as f:
    contents = [unicode(l, 'utf-8') for l in f.readlines()]

def write(contents):
    # Safe changes to file
    with open(path, "w") as f:
        contents = "".join(contents).encode('utf-8')
        f.write(contents)


# HANDLING HTML

def getFrame(url):
    url = url.replace('watch?v=', 'embed/')
    line = u'\t\t<iframe width="560" height="315" src="'
    line += url
    line += u'?autoplay=1&iv_load_policy=3" frameborder="0"></iframe>\n'
    return line

def isIframeLine(line):
    # Note that iframe
    if "<iframe" in line:
        return True
    return False


# INTERFACE

def update(url):
    # Render HTML
    htmlString = getFrame(url)
    # Add to the contents list
    for i in range(len(contents)):
        line = contents[i]
        if isIframeLine(line):
            contents[i] = htmlString
    write(contents)
    click.echo("~ ding ~")
    sys.exit(0)

@click.command()
@click.argument('url', required=False)
def main(url):
    if not url:
        url = click.prompt("URL")
    if "youtube" not in url:
        webbrowser.open("file:///Users/lukas/Desktop/programming/cym/index.html", new=2)
        return
    update(url)

if __name__ == '__main__':
    main()
