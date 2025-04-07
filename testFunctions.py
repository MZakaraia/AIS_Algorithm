import numpy as np

def ackley(x, a=20, b=0.2, c=2*np.pi):
    """
    Ackley function.
    Global minimum at f(0,0,...,0) = 0.
    """
    d = len(x)
    sum1 = np.sum(x**2)
    sum2 = np.sum(np.cos(c * x))
    term1 = -a * np.exp(-b * np.sqrt(sum1 / d))
    term2 = -np.exp(sum2 / d)
    return term1 + term2 + a + np.exp(1)

def rastrigin(x):
    """
    Rastrigin function.
    Global minimum at f(0,0,...,0) = 0.
    """
    A = 10
    n = len(x)
    return A * n + np.sum(x**2 - A * np.cos(2 * np.pi * x))

def schwefel(x):
    """
    Schwefel function.
    Global minimum at f(420.9687, ..., 420.9687) = 0.
    """
    d = len(x)
    return 418.9829 * d - np.sum(x * np.sin(np.sqrt(np.abs(x))))

def griewank(x):
    """
    Griewank function.
    Global minimum at f(0,0,...,0) = 0.
    """
    sum_term = np.sum(x**2 / 4000)
    prod_term = np.prod(np.cos(x / np.sqrt(np.arange(1, len(x) + 1))))
    return sum_term - prod_term + 1

def michalewicz(x, m=10):
    """
    Michalewicz function.
    Global minimum depends on dimensionality.
    """
    i = np.arange(1, len(x) + 1)
    return -np.sum(np.sin(x) * (np.sin(i * x**2 / np.pi))**(2 * m))

def levy(x):
    """
    Levy function.
    Global minimum at f(1,1,...,1) = 0.
    """
    w = 1 + (x - 1) / 4
    term1 = np.sin(np.pi * w[0])**2
    term2 = np.sum((w[:-1] - 1)**2 * (1 + 10 * np.sin(np.pi * w[:-1] + 1)**2))
    term3 = (w[-1] - 1)**2 * (1 + np.sin(2 * np.pi * w[-1])**2)
    return term1 + term2 + term3

def six_hump_camel(x):
    """
    Six-hump camel function.
    Global minima at f(±0.0898, ±0.7126) = -1.0316.
    """
    x1, x2 = x
    term1 = (4 - 2.1 * x1**2 + (x1**4) / 3) * x1**2
    term2 = x1 * x2
    term3 = (-4 + 4 * x2**2) * x2**2
    return term1 + term2 + term3

def eggholder(x):
    """
    Eggholder function.
    Global minimum at f(512, 404.2319) = -959.6407.
    """
    x1, x2 = x
    term1 = -(x2 + 47) * np.sin(np.sqrt(abs(x2 + x1 / 2 + 47)))
    term2 = -x1 * np.sin(np.sqrt(abs(x1 - (x2 + 47))))
    return term1 + term2

def booth(x):
    """
    Booth function.
    Global minimum at f(1, 3) = 0.
    """
    x1, x2 = x
    return (x1 + 2*x2 - 7)**2 + (2*x1 + x2 - 5)**2

def beale(x):
    """
    Beale function.
    Global minimum at f(3, 0.5) = 0.
    """
    x1, x2 = x
    term1 = (1.5 - x1 + x1 * x2)**2
    term2 = (2.25 - x1 + x1 * x2**2)**2
    term3 = (2.625 - x1 + x1 * x2**3)**2
    return term1 + term2 + term3

def himmelblau(x):
    """
    Himmelblau function.
    Global minima at f(3, 2), f(-2.805, 3.131), f(-3.779, -3.283), and f(3.584, -1.848) = 0.
    """
    x1, x2 = x
    return (x1**2 + x2 - 11)**2 + (x1 + x2**2 - 7)**2
