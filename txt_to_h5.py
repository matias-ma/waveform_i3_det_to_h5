# python3

import pandas as pd 
import os

if os.path.exists('/home/mandia/waveform/hnl/csv') is True: 
    os.system('rm -r /home/mandia/waveform/hnl/csv')
    os.mkdir('/home/mandia/waveform/hnl/csv')
else:   
    os.mkdir('/home/mandia/waveform/hnl/csv')

if os.path.exists('/home/mandia/waveform/hnl/h5') is True: 
    os.system('rm -r /home/mandia/waveform/hnl/h5')
    os.mkdir('/home/mandia/waveform/hnl/h5')
else:   
    os.mkdir('/home/mandia/waveform/hnl/h5')
    

for i in range(1,10):

    for x in range(1,25):
        os.mkdir('/home/mandia/waveform/hnl/csv/csv'+str(i)+'_'+str(x))
        os.mkdir('/home/mandia/waveform/hnl/h5/h5_'+str(i)+'_'+str(x))

        df_charge = pd.read_csv('/home/mandia/waveform/hnl/txt/txt'+str(i)+'_'+str(x)+'/charge.txt')
        c_charge = df_charge.to_csv('/home/mandia/waveform/hnl/csv/csv'+str(i)+'_'+str(x)+'/charge.csv', index = None)
        h_charge = pd.read_csv('/home/mandia/waveform/hnl/csv/csv'+str(i)+'_'+str(x)+'/charge.csv').to_hdf('/home/mandia/waveform/hnl/h5/h5_'+str(i)+'_'+str(x)+'/charge.hdf5', key='data')

        df_time = pd.read_csv('/home/mandia/waveform/hnl/txt/txt'+str(i)+'_'+str(x)+'/time.txt')
        c_time = df_time.to_csv('/home/mandia/waveform/hnl/csv/csv'+str(i)+'_'+str(x)+'/time.csv', index = None)
        h_time = pd.read_csv('/home/mandia/waveform/hnl/csv/csv'+str(i)+'_'+str(x)+'/time.csv').to_hdf('/home/mandia/waveform/hnl/h5/h5_'+str(i)+'_'+str(x)+'/time.hdf5', key='data')

        df_position = pd.read_csv('/home/mandia/waveform/hnl/txt/txt'+str(i)+'_'+str(x)+'/position.txt')
        c_position = df_position.to_csv('/home/mandia/waveform/hnl/csv/csv'+str(i)+'_'+str(x)+'/position.csv', index = None)
        h_position = pd.read_csv('/home/mandia/waveform/hnl/csv/csv'+str(i)+'_'+str(x)+'/position.csv').to_hdf('/home/mandia/waveform/hnl/h5/h5_'+str(i)+'_'+str(x)+'/position.hdf5', key='data')

        df_time_nop = pd.read_csv('/home/mandia/waveform/hnl/txt/txt'+str(i)+'_'+str(x)+'/time_nop.txt')
        c_time_nop = df_time_nop.to_csv('/home/mandia/waveform/hnl/csv/csv'+str(i)+'_'+str(x)+'/time_nop.csv', index = None)
        h_time_nop = pd.read_csv('/home/mandia/waveform/hnl/csv/csv'+str(i)+'_'+str(x)+'/time_nop.csv').to_hdf('/home/mandia/waveform/hnl/h5/h5_'+str(i)+'_'+str(x)+'/time_nop.hdf5', key='data')
        

