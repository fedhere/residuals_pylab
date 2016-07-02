import matplotlib.ticker as mpltk

import matplotlib as mpl
import pylabsetup
import numpy as np

import pylab as pl


def plotwresids(x, y, res, xerr=None, yerr=None, reserr=None, xlabel="",
                ylabel="", reslabel="residuals", xlim=None, ylim=None,
                color=['k'], alpha=[1], marker=['o'], scatter=True,
                live=False, fig=None, legend=None, loc=1):

    if live:
        pl.ion()
    if not (fig is None):
        fig = pl.figure(fig)
    else:
        fig = pl.figure()
    mpl.rcParams['font.size'] = 18.
    mpl.rcParams['font.family'] = 'serif'
    mpl.rcParams['font.serif'] = 'Times New Roman'
    mpl.rcParams['axes.labelsize'] = 18
    mpl.rcParams['xtick.labelsize'] = 18.
    mpl.rcParams['ytick.labelsize'] = 18.
    majorformatterresy = mpltk.FormatStrFormatter('%.1f')
    top_offset = .07
    left_offset = .15
    right_offset = .2
    bottom_offset = .13
    hgap = 0
    #    ax_width = 1-left_offset - right_offset
    #    ax_height = (1-top_offset - bottom_offset - hgap)/2

    left, width = 0.1, 0.65
    bottom, height = 0.1, 0.65
    bottom_h = left_h = left + width

    rect_scatter = [left, bottom + 0.2, width, height]
    rect_histx = [left, bottom, width, 0.2]
    #    rect_histy = [left_h, bottom, 0.2, height]

    pl.subplots_adjust(hspace=0., wspace=0.1)
    ax1 = pl.axes(rect_scatter)
    axres = pl.axes(rect_histx)
    ax1.minorticks_on()
    axres.minorticks_on()
    pl.setp(ax1.get_xticklabels(),
            visible=False)
    if not isinstance(x, list) and not isinstance(x, np.ndarray):
        x = [[x]]
        y = [[y]]
        res = [[res]]
        scatter = [[scatter]]
        if yerr:
            yerr = [[yerr]]
        if xerr:
            yerr = [[xerr]]
    elif not isinstance(x[0], list) and not isinstance(x[0], np.ndarray):
        x = [x]
        y = [y]
        res = [res]
        scatter = [scatter]
        if xerr:
            xerr = [xerr]
        if yerr:
            yerr = [yerr]

    if len(alpha) < len(x):
        alpha = alpha * len(x)
    if len(color) < len(x):
        color = color * len(x)
    if len(marker) < len(x):
        marker = marker * len(x)

    for i in range(len(x)):
        label = ''
        if isinstance(legend, str):
            label = legend
        elif isinstance(legend, np.ndarray) or isinstance(legend, list):
            try:
                label = legend[i]
            except IndexError:
                label = ''

        if yerr and yerr[i] is not None:
            if xerr and xerr[i] is not None:
                if scatter[i]:
                    ax1.errorbar(x[i], y[i], xerr=xerr[i], yerr=yerr[i],
                                 color=color[i], alpha=alpha[i],
                                 marker=marker[i], fmt='.', label=label)
                else:
                    ax1.errorbar(x[i], y[i], xerr=xerr[i], yerr=yerr[i],
                                 color=color[i], alpha=alpha[i],
                                 marker=marker[i], label=label)

            else:
                if scatter[i]:
                    ax1.errorbar(x[i], y[i], yerr=yerr[i], color=color[i],
                                 alpha=alpha[i], marker=marker[i],
                                 fmt='.', label=label)
                else:
                    ax1.errorbar(x[i], y[i], yerr=yerr[i], color=color[i],
                                 alpha=alpha[i], marker=marker[i], label=label)

        elif scatter:
            ax1.scatter(x[i], y[i], color=color[i], alpha=alpha[i],
                        marker=marker[i],
                        label=label)
        else:
            ax1.plot(x[i], y[i], color=color[i], alpha=alpha[i],
                     marker=marker[i],
                     label=label)
        if xlim:
            ax1.set_xlim(xlim)
        if ylim:
            ax1.set_xlim(ylim)
        if live:
            pl.draw()

        try:
            res[i].all()
            if reserr and not (reserr[i] is None):
                axres.errorbar(x[i], res[i], yerr=reserr[i], color=color[i],
                               alpha=alpha[i], fmt='.',
                               marker=marker[i], label=legend)
            axres.scatter(x[i], res[i], 20, color=color[i],
                          alpha=alpha[i], label=legend)
        except IndexError:
            pass
        if legend:
            ax1.legend(fontsize=12, loc=loc)

    majorlocatory = mpltk.MultipleLocator((axres.get_ylim()[1] -
                                           axres.get_ylim()[0]) / 3)
    axres.yaxis.set_major_locator(majorlocatory)
    axres.set_xlim(ax1.get_xlim()[0], ax1.get_xlim()[1])
    axres.plot([axres.get_xlim()[0], axres.get_xlim()[1]], [0, 0], 'k--')

    axres.set_xlabel(xlabel)
    ax1.set_ylabel(ylabel)
    axres.set_yticks(axres.get_yticks()[:-2])
    axres.set_ylabel(reslabel)
    axres.yaxis.set_major_formatter(majorformatterresy)

#    pl.show()
    return fig
