import numpy as np
import matplotlib.pyplot as plt


def f(x):
    mu = 3
    sigma = 1
    return (1/sigma*np.sqrt(2*np.pi) * np.exp((-1/2) * ((x-mu)/sigma)**2))

def main():
    N=10000 #10000 samples

    #assume normal proposal likelihood N(theta_dash, s^2)
    theta_dash = 0.5 #mean
    s = 0.1 #step size

    #initialise thetas
    thetas = np.zeros(shape=N)
    thetas[0] = theta_dash

    for i in range(1,N):
        z_star = np.random.normal() #sample from normal(0,1)
        theta_star = thetas[i-1] + s*z_star #translate by adding stdev*mean

        if np.logical_or(theta_star>1, theta_star<0): #if outside of beta dist bounds
            thetas[i] = thetas[i-1] #reject
        else: 
            ratio = f(theta_star) / f(thetas[i-1])
            if ratio < np.random.uniform(0,1):
                thetas[i] = theta_star  #if ratio less than unif, accept
            else:
                thetas[i] = thetas[i-1] #otherwise reject
    plt.hist(thetas)
    plt.show()

if __name__ == '__main__':
    main()

        