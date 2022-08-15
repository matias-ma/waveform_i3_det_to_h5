# python3

import os 
from ast import literal_eval

for i in range(1,10):
    for x in range(1,25):
        # charge
        with open('/home/mandia/waveform/hnl/txt/txt'+str(i)+'_'+str(x)+'/charge.txt', 'r') as file:
            c_data = file.read()

        c_data = c_data.replace('  Charge :', '')
        c_data = c_data.replace('\n', ',')
        with open('/home/mandia/waveform/hnl/txt/txt'+str(i)+'_'+str(x)+'/charge.txt', 'w') as file:
            file.write(c_data)
        with open('/home/mandia/waveform/hnl/txt/txt'+str(i)+'_'+str(x)+'/charge.txt', 'rb+') as filehandle:
            filehandle.seek(-1, os.SEEK_END)
            filehandle.truncate()

        # time
        with open('/home/mandia/waveform/hnl/txt/txt'+str(i)+'_'+str(x)+'/time.txt', 'r') as file:
            t_data = file.read()

        t_data = t_data.replace('  Time   :', '')
        t_data = t_data.replace('\n', ',')
        with open('/home/mandia/waveform/hnl/txt/txt'+str(i)+'_'+str(x)+'/time.txt', 'w') as file:
            file.write(t_data)
        with open('/home/mandia/waveform/hnl/txt/txt'+str(i)+'_'+str(x)+'/time.txt', 'rb+') as filehandle:
            filehandle.seek(-1, os.SEEK_END)
            filehandle.truncate()

        # position
        with open('/home/mandia/waveform/hnl/txt/txt'+str(i)+'_'+str(x)+'/position.txt', 'r') as file:
            p_data = file.read()

        p_data = p_data.replace('    Position: ', '')
        p_data = p_data.replace('\n', ',')
        with open('/home/mandia/waveform/hnl/txt/txt'+str(i)+'_'+str(x)+'/position.txt', 'w') as file:
            file.write(p_data)
        with open('/home/mandia/waveform/hnl/txt/txt'+str(i)+'_'+str(x)+'/position.txt', 'rb+') as filehandle:
            filehandle.seek(-1, os.SEEK_END)
            filehandle.truncate()

        # time_nop
        with open('/home/mandia/waveform/hnl/txt/txt'+str(i)+'_'+str(x)+'/time_nop.txt', 'r') as file:
            t_nop_data = file.read()

        t_nop_data = t_nop_data.replace('        Time: ', '')
        t_nop_data = t_nop_data.replace('\n', ',')
        with open('/home/mandia/waveform/hnl/txt/txt'+str(i)+'_'+str(x)+'/time_nop.txt', 'w') as file:
            file.write(t_nop_data)
        with open('/home/mandia/waveform/hnl/txt/txt'+str(i)+'_'+str(x)+'/time_nop.txt', 'rb+') as filehandle:
            filehandle.seek(-1, os.SEEK_END)
            filehandle.truncate()

        # time shift
        with open('/home/mandia/waveform/hnl/txt/txt'+str(i)+'_'+str(x)+'/shift.txt', 'r') as file:
            shift_data = file.read()
        shift_data = shift_data.replace('I3Double(', '')
        shift_data = shift_data.replace(')', '')
        with open('/home/mandia/waveform/hnl/txt/txt'+str(i)+'_'+str(x)+'/shift.txt', 'w') as file:
            file.write(shift_data)
