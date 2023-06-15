# Getting Points from user mouse clicks using turtle
import turtle
points = []
turtle.hideturtle()
turtle.color("white")
def get_mouse_click_coor(x, y):
    points.append((x, y))
    turtle.goto(x, y)
    turtle.dot(5,"black")

turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()


# with open("points.csv","a") as f:
#     # f.write("x,y\n")
#     for x, y in points:
#         f.write(f"{x},{y}\n")

# Serializing the points into a pickle file for future use.
import pickle
with open("points.pickle", "wb") as pl:
    pickle.dump(points, pl)

# Clustering
import matplotlib.pyplot as plt
from numpy import array

from sklearn.cluster import KMeans
model=KMeans(n_clusters=4)
model.fit(points)
points = array(points)
plt.scatter(*points.T, c=model.labels_)
plt.show()