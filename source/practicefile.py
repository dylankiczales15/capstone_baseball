import pybaseball


out_fp='../baseball_data/practice_data.csv'


x= pybaseball.statcast(start_dt='2020-08-20')
x.to_csv(out_fp)







