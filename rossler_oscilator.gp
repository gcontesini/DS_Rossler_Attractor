reset
data_pnt="ts_rossler_oscilator.dat"

set terminal png
set output "rossler_oscilator_rk4.png"
set multiplot
set grid 


set size 0.5, 0.5 
set origin 0, 0
splot data_pnt u 2:3:4 notitle w l
set origin 0, 0.5
# set xrange[0:50]
# set yrange[-20:30]
plot data_pnt u 1:2 w l title "x ts"
set origin 0.5, 0 
# set yrange[-30:40]
plot data_pnt u 1:3 w l title "y ts"
set origin 0.5, 0.5
# set yrange[0:60]
plot data_pnt u 1:4 w l title "z ts"

reset 
unset multiplot
data_pnt="ts_rossler_oscilator.dat"

# set terminal png
set grid 

set output "rossler_oscilator_attractor.png"
splot data_pnt u 2:3:4 notitle w l

set output "rossler_oscilator_x_ts.png"
plot data_pnt u 1:2 notitle w l

set output "rossler_oscilator_y_ts.png"
plot data_pnt u 1:3 notitle w l

set output "rossler_oscilator_z_ts.png"
plot data_pnt u 1:4 notitle w l


reset