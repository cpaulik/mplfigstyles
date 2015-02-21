# Matplotlib figure styles #
This is my very small collection of matplotlib styles. It also contains code to
automatically size your figure to common 1 or 2 column layouts of
scientific journals or other publications using the golden ratio.

Currently I am the only user I know of but if you also want an
installable version of your matplotlib styles feel free to use it.

## Usage ##

```python
In [1]: import matplotlib.pyplot as plt

In [2]: plt.style.available
Out[2]: [u'dark_background', u'bmh', u'grayscale', u'ggplot', u'fivethirtyeight']

In [3]: import mplfigstyles

In [4]: plt.style.available
Out[4]: 
['basic_pdf',
 u'grayscale',
 u'bmh',
 u'dark_background',
 u'ggplot',
 u'fivethirtyeight',
 'presentation']
```

After that you can use the new styles as [described here](http://matplotlib.org/users/style_sheets.html#customizing-plots-with-style-sheets) 

## Design details ##

mplfigstyles adds the figstyles directory to the
matplotlib.pyplot.style.core.USER_LIBRARY_PATHS variable and reloads
the library. To add a style please put in in this directory and submit
a PR.

