from scipy import stats
from scipy.stats import norm
import numpy as np
import pylab as pl
# x = norm(loc=6313.7258064516127,scale=68766.482882414159)
# y = norm(loc=1.0,scale=2.0)
# x = np.arange(-0,10000,0.1)
# pl.plot(t,x.pdf(t),label="$X$",color="red")
# pl.plot(t,y.pdf(t),"b--",label="$Y$")
# pl.show()
t = np.arange(-0,10000,0.001)
x = norm.pdf(t, 297.81801125703566, 262.23364178231242)
y = norm.pdf(t, 6313.7258064516127, 181.17048736405636)
z = norm.pdf(t, 1122.9285714285713, 88.47878219075568)
a = norm.pdf(t, 2284.795918367347, 204.80353747660735)
b = norm.pdf(t, 3219.5847457627119, 138.78408582821251)
c = norm.pdf(t, 3579.5, 45.089725363250253)
d = norm.pdf(t, 3816.0, 211.5060282828837)
pl.plot(t, x, label="$X$", color="red")
pl.plot(t, y, "b--", label="$Y$")
pl.plot(t, z, "r--", label="$Z$")
pl.plot(t, a, "y--", label="$A$")
pl.plot(t, b, "g--", label="$B$")
pl.plot(t, c, label="$C$", color="yellow")
pl.plot(t, d, label="D", color="black")
pl.show()