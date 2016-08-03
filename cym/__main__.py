import click, sys, os

# NOTE: change this to your html location
html = "~/Desktop/Programming Projects/cym/index.html"


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
    line += u'?autoplay=1" frameborder="0" allowfullscreen></iframe>\n'
    return line

def isIframeLine(line):
    # Note that iframe
    if "<iframe" in line:
        return True
    return False


# INTERFACE

def update():
    # Get new YouTube URL
    url = click.prompt("URL")
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
def main():
    update()

if __name__ == '__main__':
    main()