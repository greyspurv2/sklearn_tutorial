import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import SGDClassifier
from sklearn.datasets.samples_generator import make_blobs

def plot_sgd_separator():
    # we create 50 separable points
    X, Y = make_blobs(n_samples=50, centers=2,
                      random_state=0, cluster_std=0.60)

    # fit the model
    clf = SGDClassifier(loss="hinge", alpha=0.01,
                        n_iter=200, fit_intercept=True)
    clf.fit(X, Y)

    # plot the line, the points, and the nearest vectors to the plane
    xx = np.linspace(-1, 5, 10)
    yy = np.linspace(-1, 5, 10)
    # e.g.
    # array([-1.        , -0.33333333,  0.33333333,  1.        ,  1.66666667,
    #    2.33333333,  3.        ,  3.66666667,  4.33333333,  5.        ])

    X1, X2 = np.meshgrid(xx, yy) # make 2 lists comprising all 2D co-ordinate pairs
    Z = np.empty(X1.shape)
    for (i, j), val in np.ndenumerate(X1):
        x1 = val
        x2 = X2[i, j]
        decision_function_array = np.array([x1, x2]).reshape(1, -1) # e.g. [[-1.0, -1.0]]
        p = clf.decision_function(decision_function_array)        
        Z[i, j] = p[0] # confidence scores for sample (signed distance to hyperplane for each sample)
    levels = [-1.0, 0.0, 1.0]
    linestyles = ['dashed', 'solid', 'dashed']
    colors = 'k'

    ax = plt.axes()
    ax.contour(X1, X2, Z, levels, colors=colors, linestyles=linestyles)
    ax.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.Paired)

    ax.axis('tight')


if __name__ == '__main__':
    plot_sgd_separator()
    plt.show()
