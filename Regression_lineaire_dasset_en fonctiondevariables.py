import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from mpl_toolkits.mplot3d import Axes3D

######################################## Data preparation #########################################

file = r"C:\Users\pdebo\OneDrive\Documents\Cours_ESLSCA\Econometrie\Econometrie10.12.24.csv"
df = pd.read_csv(file, encoding='ISO-8859-1')
df.columns = df.columns.str.strip()  # Supprime les espaces autour des noms
print(df.columns)  # Vérifiez les noms après nettoyage
df = df[['Prix', 'Pub TV', 'Vente']]  # Garde uniquement les colonnes nécessaires


X = df[['Prix', 'Pub TV']].values.reshape(-1,2)
Y = df['Vente'].values
print(np.isnan(X).sum())  # Nombre total de NaN dans X
print(np.isnan(Y).sum())  # Nombre total de NaN dans Y


######################## Prepare model data point for visualization ###############################

x = X[:, 0]
y = X[:, 1]
z = Y

x_pred = np.linspace(7.4, 8.99, 30)    # range of price values
y_pred = np.linspace(30, 62, 60)  # range of TV ads values
xx_pred, yy_pred = np.meshgrid(x_pred, y_pred)
model_viz = np.array([xx_pred.flatten(), yy_pred.flatten()]).T

print(df.head())
print(df[['Prix', 'Pub TV', 'Vente']].dtypes)
df['Prix'] = pd.to_numeric(df['Prix'], errors='coerce')  # Convertit en nombres, remplace les erreurs par NaN
df['Pub TV'] = pd.to_numeric(df['Pub TV'], errors='coerce')
df['Vente'] = pd.to_numeric(df['Vente'], errors='coerce')

df = df.dropna()  # Supprime les lignes avec des NaN
print(df.isnull().sum())  # Nombre de valeurs manquantes par colonne

################################################ Train #############################################

ols = linear_model.LinearRegression()
model = ols.fit(X, Y)
predicted = model.predict(model_viz)

############################################## Evaluate ############################################

r2 = model.score(X, Y)

############################################## Plot ################################################

plt.style.use('default')

fig = plt.figure(figsize=(12, 4))

ax1 = fig.add_subplot(131, projection='3d')
ax2 = fig.add_subplot(132, projection='3d')
ax3 = fig.add_subplot(133, projection='3d')

axes = [ax1, ax2, ax3]

for ax in axes:
    ax.plot(x, y, z, color='k', zorder=15, linestyle='none', marker='o', alpha=0.5)
    ax.scatter(xx_pred.flatten(), yy_pred.flatten(), predicted, facecolor=(0,0,0,0), s=20, edgecolor='#70b3f0')
    ax.set_xlabel('Prix de vente', fontsize=12)
    ax.set_ylabel('TV ads', fontsize=12)
    ax.set_zlabel('Nombre de ventes', fontsize=12)
    ax.locator_params(nbins=4, axis='x')
    ax.locator_params(nbins=5, axis='x')

ax1.text2D(0.2, 0.32, 'Pierre de B.', fontsize=13, ha='center', va='center',
           transform=ax1.transAxes, color='grey', alpha=0.5)
ax2.text2D(0.3, 0.42, 'Pierre de B.', fontsize=13, ha='center', va='center',
           transform=ax2.transAxes, color='grey', alpha=0.5)
ax3.text2D(0.85, 0.85, 'Pierre de B.', fontsize=13, ha='center', va='center',
           transform=ax3.transAxes, color='grey', alpha=0.5)

ax1.view_init(elev=27, azim=112)
ax2.view_init(elev=16, azim=-51)
ax3.view_init(elev=60, azim=165)

# Save animation as GIF

# for ii in np.arange(0, 360, 1):
#    ax.view_init(elev=32, azim=ii)
#    fig.savefig('gif_image%d.png' % ii)

fig.suptitle('$R^2 = %.2f$' % r2, fontsize=20)

fig.tight_layout()

plt.show()