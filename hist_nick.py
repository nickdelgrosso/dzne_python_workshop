import numpy as np
import matplotlib
import matplotlib.pyplot as plt
print("hello")

matplotlib.style.available
matplotlib.style.use("ggplot")

#  Generate Data
data = np.random.normal(1, 1, 200)
data2 = np.random.normal(0, 1, 20000)

#  Make a histogram of the Data
fig = plt.figure()
plt.hist(data, alpha=0.4, bins=30, density=True, label="Control");
plt.hist(data2, alpha=0.5, bins=30, density=True, label="Treatment");
ax = plt.gca()
ax.set(
    xlabel="Data", 
    ylabel="Proportion", 
    title="A Histogram"
)
plt.legend()


# Display the Figure
plt.show()
fig.savefig("hist.png")
