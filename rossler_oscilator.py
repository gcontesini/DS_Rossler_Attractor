'''



'''
import numpy as np 

def main():

  # CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC TIME

  max_time_int = 2e2
  time_step_float =  0.01
  time_interval_ary = np.arange( 0, max_time_int, time_step_float )

  # CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC FILE

  out_file = open("ts_rossler_oscilator.dat","w")

  # CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC INITIAL CONDITIONS 1

  x_rk4_1_float = 1
  y_rk4_1_float = 1
  z_rk4_1_float = 1
  
  # CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC INITIAL CONDITIONS 2

  x_rk4_2_float = 1+1e-6
  y_rk4_2_float = 1+1e-6
  z_rk4_2_float = 1+1e-6

  for time_float in time_interval_ary:

  # CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC LYAPUNOV EXPONENT

    delta_x_rk4_12_float = x_rk4_1_float - x_rk4_2_float
    delta_y_rk4_12_float = y_rk4_1_float - y_rk4_2_float 
    delta_z_rk4_12_float = z_rk4_1_float - z_rk4_2_float 

    delta_init_cond_float = np.log( np.sqrt( (delta_x_rk4_12_float*delta_x_rk4_12_float)+(delta_y_rk4_12_float*delta_y_rk4_12_float)+(delta_z_rk4_12_float*delta_z_rk4_12_float) ) )

  # CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC OUTPUT

    out_file.write( str(time_float)+"\t"+str(x_rk4_1_float)+"\t"+str(y_rk4_1_float)+"\t"+str(z_rk4_1_float)+"\t"+str(delta_init_cond_float)+"\n" ) 
  
  # CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC RK1

    # x_rk1_float += lorentz_x( x_rk1_float, y_rk1_float, z_rk1_float )*time_step_float
    # y_rk1_float += lorentz_y( x_rk1_float, y_rk1_float, z_rk1_float )*time_step_float
    # z_rk1_float += lorentz_z( x_rk1_float, y_rk1_float, z_rk1_float )*time_step_float

  # CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC RK4-1

    k1x = rossler_x( x_rk4_1_float, y_rk4_1_float, z_rk4_1_float )
    k1y = rossler_y( x_rk4_1_float, y_rk4_1_float, z_rk4_1_float )
    k1z = rossler_z( x_rk4_1_float, y_rk4_1_float, z_rk4_1_float )

    k2x = rossler_x( x_rk4_1_float+(time_step_float*k1x*0.5), y_rk4_1_float, z_rk4_1_float )
    k2y = rossler_y( x_rk4_1_float, y_rk4_1_float+(time_step_float*k1y*0.5), z_rk4_1_float )
    k2z = rossler_z( x_rk4_1_float, y_rk4_1_float, z_rk4_1_float+(time_step_float*k1z*0.5) )

    k3x = rossler_x( x_rk4_1_float+(time_step_float*k2x*0.5), y_rk4_1_float, z_rk4_1_float )
    k3y = rossler_y( x_rk4_1_float, y_rk4_1_float+(time_step_float*k2y*0.5), z_rk4_1_float )
    k3z = rossler_z( x_rk4_1_float, y_rk4_1_float, z_rk4_1_float+(time_step_float*k2z*0.5) )

    k4x = rossler_x( x_rk4_1_float+(time_step_float*k3x), y_rk4_1_float, z_rk4_1_float )
    k4y = rossler_y( x_rk4_1_float, y_rk4_1_float+(time_step_float*k3y), z_rk4_1_float )
    k4z = rossler_z( x_rk4_1_float, y_rk4_1_float, z_rk4_1_float+(time_step_float*k3z) )

    x_rk4_1_float += (time_step_float/6.0)*(k1x+(2.0*k2x)+(2.0*k3x)+k4x)
    y_rk4_1_float += (time_step_float/6.0)*(k1y+(2.0*k2y)+(2.0*k3y)+k4y)
    z_rk4_1_float += (time_step_float/6.0)*(k1z+(2.0*k2z)+(2.0*k3z)+k4z)

  # CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC RK4-2

    k1x = rossler_x( x_rk4_2_float, y_rk4_2_float, z_rk4_2_float )
    k1y = rossler_y( x_rk4_2_float, y_rk4_2_float, z_rk4_2_float )
    k1z = rossler_z( x_rk4_2_float, y_rk4_2_float, z_rk4_2_float )

    k2x = rossler_x( x_rk4_1_float+(time_step_float*k1x*0.5), y_rk4_1_float, z_rk4_1_float )
    k2y = rossler_y( x_rk4_1_float, y_rk4_1_float+(time_step_float*k1y*0.5), z_rk4_1_float )
    k2z = rossler_z( x_rk4_1_float, y_rk4_1_float, z_rk4_1_float+(time_step_float*k1z*0.5) )

    k3x = rossler_x( x_rk4_1_float+(time_step_float*k2x*0.5), y_rk4_1_float, z_rk4_1_float )
    k3y = rossler_y( x_rk4_1_float, y_rk4_1_float+(time_step_float*k2y*0.5), z_rk4_1_float )
    k3z = rossler_z( x_rk4_1_float, y_rk4_1_float, z_rk4_1_float+(time_step_float*k2z*0.5) )

    k4x = rossler_x( x_rk4_1_float+(time_step_float*k3x), y_rk4_1_float, z_rk4_1_float )
    k4y = rossler_y( x_rk4_1_float, y_rk4_1_float+(time_step_float*k3y), z_rk4_1_float )
    k4z = rossler_z( x_rk4_1_float, y_rk4_1_float, z_rk4_1_float+(time_step_float*k3z) )

    x_rk4_2_float += (time_step_float/6.0)*(k1x+(2.0*k2x)+(2.0*k3x)+k4x)
    y_rk4_2_float += (time_step_float/6.0)*(k1y+(2.0*k2y)+(2.0*k3y)+k4y)
    z_rk4_2_float += (time_step_float/6.0)*(k1z+(2.0*k2z)+(2.0*k3z)+k4z)


  # CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC FILE

  out_file.close()

  # CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCLORENZA_SYTEM

def rossler_x(
    x_rk4_1_float_,
    y_rk4_1_float_,
    z_rk4_1_float_
  ):

  return (-y_rk4_1_float_-z_rk4_1_float_ )

def rossler_y(
    x_rk4_1_float_,
    y_rk4_1_float_,
    z_rk4_1_float_
  ):

  a_float = 0.2
  return (a_float*y_rk4_1_float_ + x_rk4_1_float_)

def rossler_z(
    x_rk4_1_float_,
    y_rk4_1_float_,
    z_rk4_1_float_
  ):

  b_float = 0.2
  c_float = 14
  return (b_float + z_rk4_1_float_*(x_rk4_1_float_ - c_float))


# CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC CALL MAIN

if __name__ == '__main__':
  main()