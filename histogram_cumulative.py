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

distance = 'data/distance_ori-BSF-PCF_ORIs_RNASE_G4-K_927.bed'
distance_shuffled = 'data/distance_ori_shuffled666-BSF-PCF_ORIs_RNASE_G4-K_927.bed'
df_distance = pd.read_table(distance,index_col=0)
df_distance_shuffled = pd.read_table(distance_shuffled,index_col=0)
df_distance.columns =['distance']
df_distance = df_distance.assign(type=['ori']*len(df_distance))
df_distance_shuffled.columns =['distance']
df_distance_shuffled = df_distance_shuffled.assign(type=['shuffled']*len(df_distance_shuffled))
#print(df_distance.head())
#print(df_distance_shuffled.head())
frames = [df_distance, df_distance_shuffled]
#print(frames)
distance_all = pd.concat(frames)
#print(distance_all.head())
fig, ax = plt.subplots(figsize = (12,11))

sns.set_style('darkgrid')

sns.ecdfplot(x=distance_all.distance, data=distance_all, hue='type');

plot = sns.ecdfplot(x=distance_all.distance, data=distance_all, hue='type', palette=['#882255','#44AA99'], linewidth=4);
plot.axes.set_title("",fontsize=50)
plot.set_xlabel("distance to closest G4 (bp) ",fontsize=30, labelpad=30)
plot.set_ylabel("proportion",fontsize=30, labelpad=30)
plot.tick_params(labelsize=20)
#plot.legend(title='', loc='lower right', labels=['shuffled control','origins'], fontsize=20)    
plot.legend_.remove() 

# print the distance at 80th percentile
print(distance_all.groupby('type')['distance'].quantile(.5))

# control x and y limits
plt.ylim(0, None)
plt.xlim(0,30000)

plt.show()

# fig = plt.figure(figsize=(9, 4), layout="constrained")
# axs = fig.subplots(1, 2, sharex=True, sharey=True)


