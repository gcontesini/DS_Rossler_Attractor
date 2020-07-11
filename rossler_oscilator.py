'''



'''
import numpy as np 

def main():

  # CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC TIME

  max_time_int = 2e2
  time_step_float =  0.01
  time_interval_ary = np.arange( 0, max_time_int, time_step_float )

  # CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC FILE

  out_file = open("ts_rossler_oscilator.dat","w")

  # CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC INITIAL CONDITIONS

  x_float = 1
  y_float = 1
  z_float = 1
  
  # CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC RUNGE-KUTTA 4TH

  out_file.write( str(x_float)+"\t"+str(y_float)+"\t"+str(z_float)+"\n"  )

  for time_float in time_interval_ary:

  # CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC RK1

    # x_float += lorentz_x( x_float, y_float )*time_step_float
    # y_float += lorentz_y( x_float, y_float, z_float )*time_step_float
    # z_float += lorentz_z( x_float, y_float, z_float )*time_step_float

  # CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC RK4

    k1x = rossler_x( x_float, y_float, z_float )
    k1y = rossler_y( x_float, y_float, z_float )
    k1z = rossler_z( x_float, y_float, z_float )

    k2x = rossler_x( x_float+(time_step_float*k1x*0.5), y_float, z_float )
    k2y = rossler_y( x_float, y_float+(time_step_float*k1y*0.5), z_float )
    k2z = rossler_z( x_float, y_float, z_float+(time_step_float*k1z*0.5) )

    k3x = rossler_x( x_float+(time_step_float*k2x*0.5), y_float, z_float )
    k3y = rossler_y( x_float, y_float+(time_step_float*k2y*0.5), z_float )
    k3z = rossler_z( x_float, y_float, z_float+(time_step_float*k2z*0.5) )

    k4x = rossler_x( x_float+(time_step_float*k3x), y_float, z_float )
    k4y = rossler_y( x_float, y_float+(time_step_float*k3y), z_float )
    k4z = rossler_z( x_float, y_float, z_float+(time_step_float*k3z) )

    x_float += (time_step_float/6.0)*(k1x+(2.0*k2x)+(2.0*k3x)+k4x)
    y_float += (time_step_float/6.0)*(k1y+(2.0*k2y)+(2.0*k3y)+k4y)
    z_float += (time_step_float/6.0)*(k1z+(2.0*k2z)+(2.0*k3z)+k4z)

    out_file.write( str(time_float)+"\t"+str(x_float)+"\t"+str(y_float)+"\t"+str(z_float)+"\n"  )

  out_file.close()


  # CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCLORENZA_SYTEM

def rossler_x(
    x_float_,
    y_float_,
    z_float_
  ):

  return (-y_float_-z_float_ )

def rossler_y(
    x_float_,
    y_float_,
    z_float_
  ):

  a_float = 0.2
  return (a_float*y_float_ + x_float_)

def rossler_z(
    x_float_,
    y_float_,
    z_float_
  ):

  b_float = 0.2
  c_float = 14
  return (b_float + z_float_*(x_float_ - c_float))


# CCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCCC CALL MAIN

if __name__ == '__main__':
  main()