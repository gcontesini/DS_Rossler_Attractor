# DS_Rossler_Attractor

## Method

Simpletic Runge-Kutta of 4 order.

### Global Conditions

time_step = 0.01

### Initial Conditions

x_0 = 1

y_0 = 1

z_0 = 1

for the Lyapunov calculation a $\delta=1e^{-6}$ was add to the original IC in a y-semilog scale

## Results 

![original rossler attractor](https://github.com/gcontesini/DS_Rossler_Attractor/blob/master/rossler_oscilator_attractor.png)

![x ts](https://github.com/gcontesini/DS_Rossler_Attractor/blob/master/rossler_oscilator_x_ts.png)

![y ts](https://github.com/gcontesini/DS_Rossler_Attractor/blob/master/rossler_oscilator_y_ts.png)

![z ts](https://github.com/gcontesini/DS_Rossler_Attractor/blob/master/rossler_oscilator_z_ts.png)

![Lyapunov Exponent](https://github.com/gcontesini/DS_Rossler_Attractor/blob/master/rossler_oscilator_lyapunov_exp.png)

With a lyapunov exponent of 0.088129 and a Lyapunov time of 11.347, therefore the system is deterministic and not stochastic.

## Taken's Theorem

Takens theorem states that the some dynamical structures, such as attractor, catastrophes, among others, can be recovered by analyzing the time series of one or more time series by applying a a differential or smooth manifold (a smooth map). Examples include, a time lag, a canonical transformations or a group operation  that preserve the system symmetry (Rotation, Reflection or Translation). [Sugihara Lab - Detecting Causality in Complex Ecosystems  (Science DOI: 10.1126/science.1227079  (2012))](https://deepeco.ucsd.edu/publications/#page-content)

![Reconstruction of the rossler attractor based on taken's theorem for the x TS](https://github.com/gcontesini/DS_Rossler_Attractor/blob/master/rossler_x_takens_theorem.png)



![Reconstruction of the rossler attractor based on taken's theorem for the y TS](https://github.com/gcontesini/DS_Rossler_Attractor/blob/master/rossler_y_takens_theorem.png)



![Reconstruction of the rossler attractor based on taken's theorem for the z TS](https://github.com/gcontesini/DS_Rossler_Attractor/blob/master/rossler_z_takens_theorem.png)

