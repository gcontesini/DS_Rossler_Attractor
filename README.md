# DS_Rossler_Attractor

## Method

Simpletic Runge-Kutta of 4 order

### Global Conditions

time_step = 0.01

### Initial Conditions

x_0 = 1
y_0 = 1
z_0 = 1

for the Lyapunov calculation a $\delta=1e^{-6}$ was add to the original IC.

## Results 

![original rossler attractor](https://github.com/gcontesini/DS_Rossler_Attractor/blob/master/rossler_oscilator_attractor.png)

![x ts](https://github.com/gcontesini/DS_Rossler_Attractor/blob/master/rossler_oscilator_x_ts.png)

![y ts](https://github.com/gcontesini/DS_Rossler_Attractor/blob/master/rossler_oscilator_y_ts.png)

![z ts](https://github.com/gcontesini/DS_Rossler_Attractor/blob/master/rossler_oscilator_z_ts.png)

![Lyapunov Exponent](https://github.com/gcontesini/DS_Rossler_Attractor/blob/master/rossler_oscilator_lyapunov_exp.png)

With a lyapunov exponent of 0.088129 and a Lyapunov time of 11.347 the system is deterministic and not stochastic.

## Taken's Theorem

This is black magic for sure!

![Reconstruction of the rossler attractor based on taken's theorem](https://github.com/gcontesini/DS_Rossler_Attractor/blob/master/rossler_takens_theorem.png)
