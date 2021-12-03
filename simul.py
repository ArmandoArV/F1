import plotly.graph_objects as go

import numpy as np

# Generate curve data
v1 =100 # Valor de -1 original
v2 = 3500 # Original: 1
v3 = 100 # Original: 100
coef = 3
t = np.linspace(v1, v2, v3)

# Función (1*(10**-6))*(t**3) - (0.0047)*(t**2) + (4.1719)*t+1328.7

# Setup de X Y
x = t
y = (1*(10**-6))*(t**3) - (0.0047)*(t**2) + (4.1719)*t+1328.7
xm = np.min(x) - 1.5
xM = np.max(x) + 1.5
ym = np.min(y) - 1.5
yM = np.max(y) + 1.5
N = 50
s = np.linspace(v2, v3, N)
xx = t
yy = (1*(10**-6))*(t**3) - (0.0047)*(t**2) + (4.1719)*t+1328.7


# Create figure
fig = go.Figure(
    data=[go.Scatter(x=x, y=y,
                     mode="lines",
                     line=dict(width=2, color="blue")),
          go.Scatter(x=x, y=y,
                     mode="lines",
                     line=dict(width=2, color="blue"))],
    layout=go.Layout(
        xaxis=dict(range=[xm, xM], autorange=False, zeroline=False),
        yaxis=dict(range=[ym, yM], autorange=False, zeroline=False),
        title_text="RETO FORMULA 1", hovermode="closest",
        updatemenus=[dict(type="buttons",
                          buttons=[dict(label="Play",
                                        method="animate",
                                        args=[None])])]),
    frames=[go.Frame(
        data=[go.Scatter(
            x=[xx[k]],
            y=[yy[k]],
            mode="markers",
            marker=dict(color="red", size=10))])

        for k in range(N)]
)

fig.show()
