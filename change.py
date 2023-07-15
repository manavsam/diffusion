st = ''
with open('/content/diffusion/requirements.txt', 'r', encoding='utf-8') as f:
    for line in f.readlines():

        st += line.split('==')[0]
        st += '\n'

with open('/content/diffusion/requirements.txt', 'w') as f:
    f.write(st)