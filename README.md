# Matplotlib figure styles #
This is a collection of matplotlib styles. It also contains code to
automatically size your figure to common 1 or 2 column layouts of
scientific journals or other publications using the golden ratio.

## Design details ##
mplfigstyles uses matplotlib.rc_params_from_file to load the included
templates in the figstyles directory. To add a style please put in in
this directory and submit a PR against the develop branch.

It uses the matplotlib.pyplot.styles.use and
matplotlib.pyplot.styles.context functions to apply those styles.
