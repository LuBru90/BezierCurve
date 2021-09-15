# %% imports:
import numpy as np
import matplotlib.pyplot as plt

# %% linear interpolation:
def lerp(x0, x1, t):
    return t*(x1 - x0) + x0

# %% rekursive implementation of bezier algorithm:
def genBezierCurve(points, t):
    interPoints = list()
    for i, point in enumerate(points[:-1]):
        interPoints.append(lerp(point, points[i + 1], t))
    if len(interPoints) != 1:
        return genBezierCurve(interPoints, t)
    else:
        return interPoints[0]

# %% generate bezier curve:
t = np.linspace(0, 1, 100)

listOfPoints = [
                               # [x], [y]
                    np.array([[  -1], [0]]),
                    np.array([[-3/4], [1]]),
                    np.array([[   0], [0]]),
                    np.array([[ 1/2], [1]]),
                    np.array([[  -1], [2]]),
                    np.array([[   0], [0]]),
                ]

bezierCoords = genBezierCurve(listOfPoints, t)


for i, point in enumerate(listOfPoints):
    plt.plot(point[0], point[1],
            'x',
            color = 'sienna',
            markersize = 10,
            zorder = 4,
            label = 'Points' if i == 0 else None
            )

# % 1. Vector:
plt.plot(
            [listOfPoints[0][0], listOfPoints[1][0]], # x
            [listOfPoints[0][1], listOfPoints[1][1]], # y
            '-o',
            linewidth = 1,
            color = 'goldenrod'
        )

# % 2. Vector:
plt.plot(
            [listOfPoints[-2][0], listOfPoints[-1][0]], # x
            [listOfPoints[-2][1], listOfPoints[-1][1]], # y
            '-o',
            color = 'goldenrod',
            linewidth = 1,
            label = 'Support Vectors',
        )

# % Bezier:
plt.plot(
        bezierCoords[0],
        bezierCoords[1],
        color = 'royalblue',
        label = 'Bezier Curve',
        )

plt.legend(loc = 'upper right')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Bezier Curve generation')
plt.grid(1)
plt.show()
