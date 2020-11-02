import pandas as pd
import numpy as np
import scipy.stats
import matplotlib.pyplot as plt
from scipy.stats import pearsonr


def pearson_test(a, b):

    # Takes two arguments and returns correlation and p-value.
    stat, p = pearsonr(a, b)

    print('\nCorrelation: %.3f P-Value: %.3f' % (stat, p))

    # H0: the two samples are independent.
    if p > 0.05:
        return print('\nThe two samples are independent')
    # H1: there is a dependency between the samples.
    else:
        return print('\nThe two samples are dependent.')


def mean_confidence_interval(values, confidence=0.95):
    a = 1.0 * np.array(values)
    n = len(a)
    m, se = np.mean(a), scipy.stats.sem(a)
    h = se * scipy.stats.t.ppf((1 + confidence) / 2., n-1)
    return print(m, m-h, m+h)


if __name__ == '__main__':

    # Data CSV, respective columns are then placed into series variables.
    df = pd.read_csv('FM_Data.csv', index_col=0)
    data1 = df['BP.LSE'].round(2)
    data2 = df['CL=F'].round(2)
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep']
    points = [1, 22, 41, 67, 91, 116, 142, 168, 194]

    pearson_test(data1, data2)

    # Graph style.
    plt.style.use('ggplot')

    # Sub plots.
    fig, axs = plt.subplots(2)
    fig.suptitle('BP.LSE and CL=F 02/01/20 - 11/09/20', fontsize=16, fontweight='bold')
    plt.setp(axs, xticks=points, xticklabels=months)

    axs[0].plot(df.index, data1, color='green', label='BP.LSE')
    axs[0].legend(loc='upper right')
    axs[0].set_xticklabels(axs[0].get_xticklabels(), fontweight='bold', fontsize=16)
    axs[0].set(ylabel='PRICE (GBP)')

    axs[1].plot(df.index, data2, color='red', label='CL=F')
    axs[1].legend(loc='upper right')
    axs[1].set_xticklabels(axs[1].get_xticklabels(), fontweight='bold', fontsize=16)
    axs[1].set(ylabel='PRICE (USD)')

    # Label loop.
    for ax in axs.flat:
        ax.yaxis.label.set_color('black')

    plt.show()
