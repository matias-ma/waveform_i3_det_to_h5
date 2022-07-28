# python3

# charge
with open('./txt/charge.txt', 'r') as file:
    c_data = file.read()

c_data = c_data.replace('  Charge :', '')
c_data = c_data.replace('\n', ',')
with open('./txt/charge.txt', 'w') as file:
    file.write(c_data)

# time
with open('./txt/time.txt', 'r') as file:
    t_data = file.read()

t_data = t_data.replace('  Time   :', '')
t_data = t_data.replace('\n', ',')
with open('./txt/time.txt', 'w') as file:
    file.write(t_data)

# position
with open('./txt/position.txt', 'r') as file:
    p_data = file.read()

p_data = p_data.replace('    Position: ', '')
p_data = p_data.replace('\n', ',')
with open('./txt/position.txt', 'w') as file:
    file.write(p_data)

# time_nop
with open('./txt/time_nop.txt', 'r') as file:
    t_nop_data = file.read()

t_nop_data = t_nop_data.replace('        Time: ', '')
t_nop_data = t_nop_data.replace('\n', ',')
with open('./txt/time_nop.txt', 'w') as file:
    file.write(t_nop_data)
