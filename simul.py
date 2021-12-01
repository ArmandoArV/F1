import plotly.graph_objects as go

import numpy as np
# Función (1*(10**-6))*(t**3) - (0.0047)*(t**2) + (4.1719)*t

# Info de la curva
v1 = -1 # Valor de -1 original
v2 = 1 # Original: 1
v3 = 1000 # Original: 100
coef = 3
t = np.linspace(v1, v2, v3)
x = (1*(10**-6))*(t**3) - (0.0047)*(t**2) + (4.1719)*t# t+t**2
y = t+t**coef # t-t**2
xm = np.min(x) - 1.5
xM = np.max(x) + 1.5
ym = np.min(y) - 1.5
yM = np.max(y) + 1.5
N = 100 # Ene: 50
s1 = -1 # Orginal -1
s2 = 1 # Original 1
s = np.linspace(s1, s2, N)

xx = s + s ** 2
yy = s - s ** 2
vx = 1 + 2 * s
vy = 1 - 2 * s  # v=(vx, vy) velocidad
speed = np.sqrt(vx ** 2 + vy ** 2)
ux = vx / speed  # (ux, uy) tangente del vector , (-uy, ux) unidad del vector normal
uy = vy / speed

xend = xx + ux  # coords del vector tangente  (xx, yy)
yend = yy + uy

xnoe = xx - uy  # end coordinates for the unit normal vector at (xx,yy)
ynoe = yy + ux


# Create figure
fig = go.Figure(
    data=[go.Scatter(x=x, y=y,
                     name="CARRO",
                     mode="lines",
                     line=dict(width=2, color="red")),
          go.Scatter(x=x, y=y,
                     name="PISTA",
                     mode="lines",
                     line=dict(width=2, color="blue"))
          ],
    layout=go.Layout(width=600, height=600,
                     xaxis=dict(range=[xm, xM], autorange=False, zeroline=False),
                     yaxis=dict(range=[ym, yM], autorange=False, zeroline=False),
                     title="RETO | FÓRMULA 1",
                     hovermode="closest",
                     updatemenus=[dict(type="buttons",
                                       buttons=[dict(label="Play",
                                                     method="animate",
                                                     args=[None])])]),

    frames=[go.Frame(
        data=[go.Scatter(
            x=[xx[k], xend[k], None, xx[k], xnoe[k]],
            y=[yy[k], yend[k], None, yy[k], ynoe[k]],
            mode="lines",
            line=dict(color="red", width=2))
        ]) for k in range(N)]
)

fig.show()