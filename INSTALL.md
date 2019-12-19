### [Pygments](http://pygments.org/)

#### Install using Git

If you are a git user, you can install the theme and keep up to date by cloning the repo:

    $ git clone https://github.com/dracula/pygments.git

#### Install manually

Download using the [GitHub .zip download](https://github.com/dracula/pygments/archive/master.zip) option and unzip them.

#### Activating theme

You can generate the CSS stylesheet (also included in this repository) by using the included `dracula.py` file and the [Pygments Command Line Interface](http://pygments.org/docs/cmdline/):

1.  [Download Pygments](http://pygments.org/download/) on your machine
2.  Run the following command on your terminal:
    
        pygmentize -S dracula -f html > dracula.css
