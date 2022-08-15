# python3

from icecube import icetray,dataio,dataclasses, simclasses, recclasses
import os


if os.path.exists('/home/mandia/waveform/hnl/txt') is True: 
    os.system('rm -r /home/mandia/waveform/hnl/txt')
    os.mkdir('/home/mandia/waveform/hnl/txt')
else:   
    os.mkdir('/home/mandia/waveform/hnl/txt')
    
if os.path.exists('/home/mandia/waveform/hnl/not_important') is True: 
    os.system('rm -r /home/mandia/waveform/hnl/not_important')
    os.mkdir('/home/mandia/waveform/hnl/not_important')
else:   
    os.mkdir('/home/mandia/waveform/hnl/not_important')

for i in range(1,10):
       for x in range(1,25):
              os.mkdir('/home/mandia/waveform/hnl/txt/txt'+str(i)+'_'+str(x))
              os.mkdir('/home/mandia/waveform/hnl/not_important/not_important'+str(i)+'_'+str(x))
              if i<9.5:
                     f = dataio.I3File('/data/ana/BSM/HNL/MC/190607/Ares/IC86.AVG/Det/domeff_0.97/00001-01000/Det_00_11_0000'+str(i)+'.i3.zst')
              elif 9.5<i<99.5:
                     f = dataio.I3File('/data/ana/BSM/HNL/MC/190607/Ares/IC86.AVG/Det/domeff_0.97/00001-01000/Det_00_11_000'+str(i)+'.i3.zst')
              for z in range(x):
                     frame = f.pop_daq()
              pulse = frame['MCPESeriesMap_withNoise_weighted']
              nop = frame['I3Photons']
              shift = frame['TimeShift']

              with open('/home/mandia/waveform/hnl/txt/txt'+str(i)+'_'+str(x)+'/shift.txt', 'a+') as f:
                     f.write(str(shift))

              bad_words = 'Weight', 'Wavelength', 'ModuleKey', 'ParticleID', 'Group Vel.', 'Azimuth', 'Zenith', 'OMKey', 'Source', 'I3MCPulse'


              with open('/home/mandia/waveform/hnl/not_important/not_important'+str(i)+'_'+str(x)+'/pulse.txt', 'a+') as f:
                     for line in pulse:
                            f.write(str(line))
                            f.write('\n')
              with open('/home/mandia/waveform/hnl/not_important/not_important'+str(i)+'_'+str(x)+'/nop.txt', 'a+') as f:
                     for line in nop:
                            f.write(str(line))
                            f.write('\n')
              
              with open('/home/mandia/waveform/hnl/not_important/not_important'+str(i)+'_'+str(x)+'/pulse.txt', 'r+') as f:
                     for line in pulse:
                            f.write(str(line))
                            f.write('\n')
              with open('/home/mandia/waveform/hnl/not_important/not_important'+str(i)+'_'+str(x)+'/nop.txt', 'r+') as f:
                     for line in nop:
                            f.write(str(line))
                            f.write('\n')
              
              in_pulse = open('/home/mandia/waveform/hnl/not_important/not_important'+str(i)+'_'+str(x)+'/pulse.txt', 'a+')
              in_nop = open('/home/mandia/waveform/hnl/not_important/not_important'+str(i)+'_'+str(x)+'/nop.txt', 'a+')

              new_pulse = open('/home/mandia/waveform/hnl/not_important/not_important'+str(i)+'_'+str(x)+'/new_pulse.txt', 'a+')
              new_nop = open('/home/mandia/waveform/hnl/not_important/not_important'+str(i)+'_'+str(x)+'/new_nop.txt', 'a+')


              charge = open('/home/mandia/waveform/hnl/txt/txt'+str(i)+'_'+str(x)+'/charge.txt', 'a+')
              time = open('/home/mandia/waveform/hnl/txt/txt'+str(i)+'_'+str(x)+'/time.txt', 'a+')
              time_nop = open('/home/mandia/waveform/hnl/txt/txt'+str(i)+'_'+str(x)+'/time_nop.txt', 'a+')
              position = open('/home/mandia/waveform/hnl/txt/txt'+str(i)+'_'+str(x)+'/position.txt', 'a+')

              in_pulse = open('/home/mandia/waveform/hnl/not_important/not_important'+str(i)+'_'+str(x)+'/pulse.txt', 'r+')
              in_nop = open('/home/mandia/waveform/hnl/not_important/not_important'+str(i)+'_'+str(x)+'/nop.txt', 'r+')

              new_pulse = open('/home/mandia/waveform/hnl/not_important/not_important'+str(i)+'_'+str(x)+'/new_pulse.txt', 'r+')
              new_nop = open('/home/mandia/waveform/hnl/not_important/not_important'+str(i)+'_'+str(x)+'/new_nop.txt', 'r+')


              charge = open('/home/mandia/waveform/hnl/txt/txt'+str(i)+'_'+str(x)+'/charge.txt', 'r+')
              time = open('/home/mandia/waveform/hnl/txt/txt'+str(i)+'_'+str(x)+'/time.txt', 'r+')
              time_nop = open('/home/mandia/waveform/hnl/txt/txt'+str(i)+'_'+str(x)+'/time_nop.txt', 'r+')
              position = open('/home/mandia/waveform/hnl/txt/txt'+str(i)+'_'+str(x)+'/position.txt', 'r+')




              for line in in_pulse :
                     if not any(bad_word in line for bad_word in bad_words):
                            new_pulse.write(line)

              for line in in_nop :
                     if not any(bad_word in line for bad_word in bad_words):
                            new_nop.write(line)

              for line in new_pulse :
                     if 'Charge' not in line:
                            time.write(line)
                     if 'Time' not in line:
                            charge.write(line)
              for line in new_nop :
                     if 'Position' not in line:
                            time_nop.write(line)
                     if 'Time' not in line:
                            position.write(line)


              in_pulse = open('/home/mandia/waveform/hnl/not_important/not_important'+str(i)+'_'+str(x)+'/pulse.txt', 'r+')
              in_nop = open('/home/mandia/waveform/hnl/not_important/not_important'+str(i)+'_'+str(x)+'/nop.txt', 'r+')

              new_pulse = open('/home/mandia/waveform/hnl/not_important/not_important'+str(i)+'_'+str(x)+'/new_pulse.txt', 'r+')
              new_nop = open('/home/mandia/waveform/hnl/not_important/not_important'+str(i)+'_'+str(x)+'/new_nop.txt', 'r+')

              charge = open('/home/mandia/waveform/hnl/txt/txt'+str(i)+'_'+str(x)+'/charge.txt', 'r+')
              time = open('/home/mandia/waveform/hnl/txt/txt'+str(i)+'_'+str(x)+'/time.txt', 'r+')
              time_nop = open('/home/mandia/waveform/hnl/txt/txt'+str(i)+'_'+str(x)+'/time_nop.txt', 'r+')
              position = open('/home/mandia/waveform/hnl/txt/txt'+str(i)+'_'+str(x)+'/position.txt', 'r+')



              for line in in_pulse :
                     if not any(bad_word in line for bad_word in bad_words):
                            new_pulse.write(line)

              for line in in_nop :
                     if not any(bad_word in line for bad_word in bad_words):
                            new_nop.write(line)

              for line in new_pulse :
                     if 'Charge' not in line:
                            time.write(line)
                     if 'Time' not in line:
                            charge.write(line)
              for line in new_nop :
                     if 'Position' not in line:
                            time_nop.write(line)
                     if 'Time' not in line:
                            position.write(line)
