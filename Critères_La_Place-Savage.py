#Calcul et mise en commun des critères de La Place, Savage, MinMax, MaxMin, MaxMax
#Importer les bonnes bibliothèques
import math
import scipy.stats as sc
import pandas as pd
import random

def la_place_criterion(x, y):

    # Calcul de la moyenne des données
    x_mean = sum(x) / len(x)
    y_mean = sum(y) / len(y)

    # Calcul de la variance des données
    x_var = sum((xi - x_mean) ** 2 for xi in x) / len(x)
    y_var = sum((yi - y_mean) ** 2 for yi in y) / len(y)

    # Calcul du coefficient de corrélation de Pearson
    corr_coef = sum((xi - x_mean) * (yi - y_mean) for xi, yi in zip(x, y)) / (len(x) * math.sqrt(x_var * y_var))
    
    # Calcul du critère de La Place
    la_place_criterion = abs(corr_coef) * math.sqrt((len(x) - 2) / (1 - corr_coef ** 2))
    
    return la_place_criterion

def savage_criterion(x, y):
    # Calcul de la moyenne des données
    x_mean = sum(x) / len(x)
    y_mean = sum(y) / len(y)
    
    # Calcul de la variance des données
    x_var = sum((xi - x_mean) ** 2 for xi in x) / len(x)
    y_var = sum((yi - y_mean) ** 2 for yi in y) / len(y)
    
    # Calcul du coefficient de corrélation de Pearson
    corr_coef = sum((xi - x_mean) * (yi - y_mean) for xi, yi in zip(x, y)) / (len(x) * math.sqrt(x_var * y_var))
    
    # Calcul du critère de Savage
    savage_criterion = abs(corr_coef) * math.sqrt((len(x) - 2) / (1 - corr_coef ** 2)) * (len(x) - 3) / (len(x) - len(set(x)) - len(set(y)) + 2)
    
    return savage_criterion

def minmax_criterion(x, y):
    # Calcul de la moyenne des données
    x_mean = sum(x) / len(x)
    y_mean = sum(y) / len(y)
    
    # Calcul de la variance des données
    x_var = sum((xi - x_mean) ** 2 for xi in x) / len(x)
    y_var = sum((yi - y_mean) ** 2 for yi in y) / len(y)
    
    # Calcul du coefficient de corrélation de Pearson
    corr_coef = sum((xi - x_mean) * (yi - y_mean) for xi, yi in zip(x, y)) / (len(x) * math.sqrt(x_var * y_var))
    
    # Calcul du critère de MinMax
    minmax_criterion = abs(corr_coef) * math.sqrt((len(x) - 2) / (1 - corr_coef ** 2)) * math.sqrt(len(x) * len(y))
    
    return minmax_criterion

def maxmin_criterion(x, y):
    # Calcul de la moyenne des données
    x_mean = sum(x) / len(x)
    y_mean = sum(y) / len(y)
    
    # Calcul de la variance des données
    x_var = sum((xi - x_mean) ** 2 for xi in x) / len(x)
    y_var = sum((yi - y_mean) ** 2 for yi in y) / len(y)
    
    # Calcul du coefficient de corrélation de Pearson
    corr_coef = sum((xi - x_mean) * (yi - y_mean) for xi, yi in zip(x, y)) / (len(x) * math.sqrt(x_var * y_var))
    
    # Calcul du critère de MaxMin
    maxmin_criterion = abs(corr_coef) * math.sqrt((len(x) - 2) / (1 - corr_coef ** 2)) * math.sqrt(len(x) * len(y)) / (len(x) - len(set(x)) - len(set(y)) + 2)
    
    return maxmin_criterion

def maxmax_criterion(x, y):
    # Calcul de la moyenne des données
    x_mean = sum(x) / len(x)
    y_mean = sum(y) / len(y)
    
    # Calcul de la variance des données
    x_var = sum((xi - x_mean) ** 2 for xi in x) / len(x)
    y_var = sum((yi - y_mean) ** 2 for yi in y) / len(y)
    
    # Calcul du coefficient de corrélation de Pearson
    corr_coef = sum((xi - x_mean) * (yi - y_mean) for xi, yi in zip(x, y)) / (len(x) * math.sqrt(x_var * y_var))
    
    # Calcul du critère de MaxMax
    maxmax_criterion = abs(corr_coef) * math.sqrt((len(x) - 2) / (1 - corr_coef ** 2)) * math.sqrt(len(x) * len(y)) / (len(x) - len(set(x)) - len(set(y)) + 2) * (len(x) - len(set(x)) - len(set(y)) + 3)
    
    return maxmax_criterion

# Test avec des données aléatoires

x = [random.uniform(0, 1) for _ in range(100)]
y = [random.uniform(0, 1) for _ in range(100)]

print("Critère de La Place:", la_place_criterion(x, y))

print("Critère de Savage:", savage_criterion(x, y))

print("Critère de MinMax:", minmax_criterion(x, y))

print("Critère de MaxMin:", maxmin_criterion(x, y))

print("Critère de MaxMax:", maxmax_criterion(x, y))

# Test avec des données réelles - Uncomment if needed

# data = pd.read_csv("example_data.csv")

# x = data["Variable X"].tolist()

# y = data["Variable Y"].tolist()

# print("Critère de La Place:", la_place_criterion(x, y))

# print("Critère de Savage:", savage_criterion(x, y))

# print("Critère de MinMax:", minmax_criterion(x, y))

# print("Critère de MaxMin:", maxmin_criterion(x, y))

# print("Critère de MaxMax:", maxmax_criterion(x, y))