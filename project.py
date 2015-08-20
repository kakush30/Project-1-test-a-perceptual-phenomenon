__author__ = "Arpit Kanodia"

import pandas
import scipy.stats
import numpy as np
import matplotlib.pyplot as plot
import matplotlib.mlab as mlab

def ttest(filename):
    df = pandas.read_csv(filename)
    congurent = df['Congruent']
    incongurent = df['Incongruent']
    result = scipy.stats.ttest_rel(incongurent, congurent)
    print result
    
def plot_congurent(filename):
    df = pandas.read_csv(filename)
    df['Sample Number'] = df.index+1
    x = df['Sample Number']
    y = df['Congruent']
    colors = 'yellow'
    area = np.pi*20  

    fig = plot.figure()
    fig.suptitle('Congruent: ', fontsize=20, fontweight='bold')
    ax = fig.add_subplot(110)
    fig.subplots_adjust(top=0.85)
    
    ax.set_xlabel('Sample Number')
    ax.set_ylabel('Completion Time (in sec)')

    plot.xticks(np.arange(min(x), max(x)+1, 1.0))
    plot.yticks(np.arange(0, 35, 2))
    plot.scatter(x, y, s=area, c=colors, alpha=1)
    plot.ylim([0,35])
    plot.xlim([0,24])
    plot.show()

def plot_incongurent(filename):
    df = pandas.read_csv(filename)
    df['Sample Number'] = df.index+1
    x = df['Sample Number']
    y = df['Incongruent']
    colors = 'green'
    area = np.pi*20  

    fig = plot.figure()
    fig.suptitle('Incongruent: ', fontsize=20, fontweight='bold')
    ax = fig.add_subplot(110)
    fig.subplots_adjust(top=0.85)
    
    ax.set_xlabel('Sample Number')
    ax.set_ylabel('Completion Time (in sec)')

    plot.xticks(np.arange(min(x), max(x)+1, 1.0))
    plot.yticks(np.arange(0, 35, 2))
    plot.scatter(x, y, s=area, c=colors, alpha=1)
    plot.ylim([0,35])
    plot.xlim([0,24])
    plot.show()  
   
    
   
def plot_normal_distribution_congurent(filename):
    df = pandas.read_csv(filename)
    congurent = df['Congruent']
    congurent_mean = congurent.mean()
    congurent_std = congurent.std()
    range = np.arange(0, 30, 0.5)
    plot.figure().suptitle('Congruent: ', fontsize=20, fontweight='bold')
    plot.plot(range, mlab.normpdf(range,congurent_mean,congurent_std)) 
    
def plot_normal_distribution_incongurent(filename):
    df = pandas.read_csv(filename)
    incongurent = df['Incongruent']
    incongurent_mean = incongurent.mean()
    incongurent_std = incongurent.std()
    range = np.arange(0, 45, 0.5)
    plot.figure().suptitle('Incongruent: ', fontsize=20, fontweight='bold')
    plot.plot(range, mlab.normpdf(range,incongurent_mean,incongurent_std))    
    
if __name__ == '__main__':
       print ttest('stroopdata.csv')
       print plot_congurent('stroopdata.csv')
       print plot_incongurent('stroopdata.csv')
       print plot_normal_distribution_congurent('stroopdata.csv')
       print plot_normal_distribution_incongurent('stroopdata.csv')