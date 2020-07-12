awk -F "\t" '$1 {print $2}' ts_rossler_oscilator.dat > takens_no_lag.dat
awk -F "\t" '$1>0.30 {print $2}' ts_rossler_oscilator.dat > takens_first_lag.dat
awk -F "\t" '$1>0.60 {print $2}' ts_rossler_oscilator.dat > takens_second_lag.dat

paste takens_no_lag.dat takens_first_lag.dat takens_second_lag.dat | awk 'NR<19940 {print NR "\t" $0}' > takens_data_pnt.dat

rm takens_no_lag.dat
rm takens_first_lag.dat
rm takens_second_lag.dat