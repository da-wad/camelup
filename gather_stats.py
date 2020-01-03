import sys
import matplotlib.pyplot as plt
from matplotlib import colors
from matplotlib.ticker import PercentFormatter

from camels import play_game

outfile = sys.argv[1]

if __name__ == "__main__":
    n_rolls_samples = []
    realizations = 1000000
    for n in range(realizations):
        winner, n_rolls, final_game_board = play_game()
        n_rolls_samples.append(n_rolls)
        print("  {:5.1f}%     ".format(n/realizations * 100), end="\r")
    
    n_bins = max(n_rolls_samples) - min(n_rolls_samples) + 1
    fig, axs = plt.subplots(1, 1)

    N, bins, patches = axs.hist(n_rolls_samples, bins=n_bins, density=True)
    fracs = N / N.max()
    norm = colors.Normalize(fracs.min(), fracs.max())

    for thisfrac, thispatch in zip(fracs, patches):
        color = plt.cm.viridis(norm(thisfrac))
        thispatch.set_facecolor(color)

    axs.yaxis.set_major_formatter(PercentFormatter(xmax=1))
    plt.xticks(ticks=range(min(n_rolls_samples), max(n_rolls_samples)))
    fig.set_size_inches(18.5, 10.5)
    plt.savefig(outfile)
        
