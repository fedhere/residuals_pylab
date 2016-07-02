import matplotlib as mpl
import pylab as plt



def run_setup():
    mpl.rcParams.update(mpl.rcParamsDefault)
    mpl.rcParams['font.size'] = 26.
    mpl.rcParams['font.family'] = 'serif'
    #mpl.rcParams['font.family'] = 'serif'
    mpl.rcParams['font.serif'] = [  'Times New Roman',
                                    'Times','Palatino',
                                    'Charter', 'serif']
    mpl.rcParams['font.sans-serif'] = ['Helvetica']
    mpl.rcParams['axes.labelsize'] = 24
    mpl.rcParams['xtick.labelsize'] = 22.
    mpl.rcParams['ytick.labelsize'] = 22.
    mpl.rcParams['xtick.major.size']= 10.
    mpl.rcParams['xtick.minor.size']= 8.
    mpl.rcParams['ytick.major.size']= 10.
    mpl.rcParams['ytick.minor.size']= 8.
    
    mpl.rc('axes',**{'labelweight':'normal', 'linewidth':1})
    mpl.rc('axes',**{'labelweight':'normal', 'linewidth':1})
    mpl.rc('ytick',**{'major.pad':5, 'color':'k'})
    mpl.rc('xtick',**{'major.pad':5, 'color':'k'})
    
    #legend parameters too
    params = {'legend.fontsize': 24,
              'legend.numpoints':1,
              'legend.handletextpad':1
    }

    plt.rcParams.update(params)   
    plt.minorticks_on()




