import numpy as np
import matplotlib.pyplot as plt

def main():
    N = 10000 #number of samples
    U1 = np.random.rand(N)
    U2 = np.random.rand(N)

    x1 = np.sqrt(-2*np.log(U1))*np.cos(2*np.pi*U2)
    x2 = np.sqrt(-2*np.log(U1))*np.sin(2*np.pi*U2)

    plt.figure(figsize=(8,8))
    plt.scatter(x1,x2)
    plt.show()


if __name__ == '__main__':
    main()