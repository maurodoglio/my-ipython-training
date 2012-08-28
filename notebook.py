# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <headingcell level=1>

# My first IPython notebook

# <headingcell level=2>

# This is just an example to learn Ipython notebook

# <headingcell level=3>

# An example of plotting

# <codecell>

from matplotlib import pyplot as plt
import numpy as np
m = np.random.random_sample((10,10))
plt.matshow(m)

# <headingcell level=3>

# An example of embedded image

# <codecell>

from IPython.core.display import Image
Image('http://www.google.it/images/srpr/logo3w.png')

# <codecell>


