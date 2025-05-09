# -*- coding: utf-8 -*-
"""EEG Data Visualization and Signal Processing in Python.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AxtKmB_GIwySNkCrckC8AlKkKR2lx40N

**Pooch Module Error**
"""

# prompt: import mne

!pip install mne
import mne
mne.datasets.somato.data_path() # fetching somatosensory data

import mne
data_path = mne.datasets.somato.data_path()
print(data_path)

"""**Loading and Viewing Raw Data**"""

import os
path = os.path.join(data_path, 'sub-01', 'meg', 'sub-01_task-somato_meg.fif')
raw = mne.io.read_raw_fif(path)

raw.info.get('nchan') # number of channels

raw.plot()

# EDF Files
path = mne.datasets.eegbci.load_data(1, 1) # Note: 1.2 MB
path[0]
# You can double check that the file is there by doing `cat path[0]`
# to see the file contents. It'll look like a bunch of random characters and question marks

path
path[0]

# load the EDF file
raw = mne.io.read_raw_edf(path[0], preload=True)

raw.plot()

raw.set_eeg_reference()  # set reference

raw.compute_psd().plot()

filtered = raw.filter(0.5, 30)

filtered.compute_psd().plot()







