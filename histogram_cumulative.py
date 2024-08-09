"""
=================================
Plotting cumulative distributions
=================================

This example shows how to plot the empirical cumulative distribution function
(ECDF) of a sample. We also show the theoretical CDF.

In engineering, ECDFs are sometimes called "non-exceedance" curves: the y-value
for a given x-value gives probability that an observation from the sample is
below that x-value. For example, the value of 220 on the x-axis corresponds to
about 0.80 on the y-axis, so there is an 80% chance that an observation in the
sample does not exceed 220. Conversely, the empirical *complementary*
cumulative distribution function (the ECCDF, or "exceedance" curve) shows the
probability y that an observation from the sample is above a value x.

A direct method to plot ECDFs is `.Axes.ecdf`.  Passing ``complementary=True``
results in an ECCDF instead.

Alternatively, one can use ``ax.hist(data, density=True, cumulative=True)`` to
first bin the data, as if plotting a histogram, and then compute and plot the
cumulative sums of the frequencies of entries in each bin.  Here, to plot the
ECCDF, pass ``cumulative=-1``.  Note that this approach results in an
approximation of the E(C)CDF, whereas `.Axes.ecdf` is exact.
"""
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns

distance = 'data/distance_ori-PCF-BST_G4hunter_427-2018_sorted.bed'
distance_shuffled = 'data/distance_ori-shuffled666-PCF-BST_G4hunter_427-2018_sorted.bed'
df_distance = pd.read_table(distance,index_col=0)
df_distance_shuffled = pd.read_table(distance_shuffled,index_col=0)
df_distance.columns =['distance']
df_distance = df_distance.assign(type=['ori']*len(df_distance))
df_distance_shuffled.columns =['distance']
df_distance_shuffled = df_distance_shuffled.assign(type=['control']*len(df_distance_shuffled))
#print(df_distance.head())
#print(df_distance_shuffled.head())
frames = [df_distance, df_distance_shuffled]
print(frames)
distance_all = pd.concat(frames)
print(distance_all.head())

sns.set_style('darkgrid')

sns.ecdfplot(x=distance_all.distance, data=distance_all, hue='type');

# fig = plt.figure(figsize=(9, 4), layout="constrained")
# axs = fig.subplots(1, 2, sharex=True, sharey=True)


# #Cumulative distributions.
# axs[0].ecdf(df_distance, label="CDF")
# n, bins, patches = axs[0].hist(df_distance, n_bins, density=True, histtype="step",cumulative=True, label="Cumulative histogram")
# x = np.linspace(df_distance.min(), df_distance.max())
# y = ((1 / (np.sqrt(2 * np.pi) * sigma)) *
#      np.exp(-0.5 * (1 / sigma * (x - mu))**2))
# y = y.cumsum()
# y /= y[-1]
# axs[0].plot(x, y, "k--", linewidth=1.5, label="Theory")

# # Complementary cumulative distributions.
# axs[1].ecdf(data, complementary=True, label="CCDF")
# axs[1].hist(data, bins=bins, density=True, histtype="step", cumulative=-1,
#             label="Reversed cumulative histogram")
# axs[1].plot(x, 1 - y, "k--", linewidth=1.5, label="Theory")

# Label the figure.
# fig.suptitle("Cumulative distributions")
# for ax in axs:
#     ax.grid(True)
#     ax.legend()
#     ax.set_xlabel("Annual rainfall (mm)")
#     ax.set_ylabel("Probability of occurrence")
#     ax.label_outer()

plt.show()

# %%
#
# .. admonition:: References
#
#    The use of the following functions, methods, classes and modules is shown
#    in this example:
#
#    - `matplotlib.axes.Axes.hist` / `matplotlib.pyplot.hist`
#    - `matplotlib.axes.Axes.ecdf` / `matplotlib.pyplot.ecdf`
