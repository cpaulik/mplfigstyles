from ._version import get_versions

__version__ = get_versions()['version']
del get_versions

import matplotlib.pyplot as plt
import os


# add mplfigstyle defined styles to matplotlib styles
plt.style.core.USER_LIBRARY_PATHS.append(
    os.path.join(os.path.split(os.path.abspath(__file__))[0], "figstyles"))
plt.style.reload_library()
