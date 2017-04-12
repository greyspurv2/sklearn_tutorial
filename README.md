# Scikit-learn Tutorial

Original author: *Jake VanderPlas*

- email: <jakevdp@uw.edu>
- twitter: [@jakevdp](https://twitter.com/jakevdp)
- github: [jakevdp](http://github.com/jakevdp)

This repository contains notebooks and other files associated with my
[Scikit-learn](http://scikit-learn.org) tutorial.

This _fork_ is by Ian Ozsvald, this contains light edits for Python 3.5+ in 2017 along with some re-ordering. No fundamental changes have been made. Full attribution goes to Jake for writing this tutorial. Slight change below to the `conda` setup. The most relevant of Jake's videos to this tutorial seems to be from PyCon 2015: https://www.youtube.com/watch?v=L7R4HUQ-eQ0

## Installation Notes
This tutorial requires the following packages:

- Python version 2.6-2.7 or 3.3+
- `numpy` version 1.5 or later: http://www.numpy.org/
- `scipy` version 0.10 or later: http://www.scipy.org/
- `matplotlib` version 1.3 or later: http://matplotlib.org/
- `scikit-learn` version 0.14 or later: http://scikit-learn.org
- `ipython` version 2.0 or later, with notebook support: http://ipython.org
- `seaborn` version 0.5 or later

The easiest way to get these is to use the [conda](https://store.continuum.io/) environment manager.
I suggest downloading and installing [miniconda](http://conda.pydata.org/miniconda.html).

Once this is installed, the following command will install all required packages in your Python environment:
```
$ conda create -n cluj_training_day python=3.5 numpy scipy matplotlib scikit-learn jupyter seaborn
$ source activate cluj_training_day
$ jupyter notebook # will start a web browser-based Notebook

```

Alternatively, you can download and install the (very large) Anaconda software distribution, found at https://store.continuum.io/.

## Downloading the Tutorial Materials
I would highly recommend using git, not only for this tutorial, but for the
general betterment of your life.  Once git is installed, you can clone the
material in this tutorial by using the git address shown above:

    git clone git://github.com/jakevdp/sklearn_tutorial.git

If you can't or don't want to install git, there is a link above to download
the contents of this repository as a zip file.  I may make minor changes to
the repository in the days before the tutorial, however, so cloning the
repository is a much better option.


## Notebook Listing
You can [view the tutorial materials](http://nbviewer.ipython.org/github/jakevdp/sklearn_tutorial/blob/master/notebooks/Index.ipynb) using the excellent nbviewer service.

Note, however, that you cannot modify or run the contents within nbviewer.
To modify them, first download the tutorial repository, change to the notebooks directory, and run ``ipython notebook``.
You should see the list in the ipython notebook launch page in your web browser.
For more information on the IPython notebook, see http://ipython.org/notebook.html

Note also that some of the code in these notebooks will not work outside the
directory structure of this tutorial, so it is important to clone the full
repository if possible.
