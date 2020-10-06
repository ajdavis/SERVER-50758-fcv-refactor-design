import subprocess

subprocess.call(['quilt', 'pop', '-a'])

subprocess.check_call(
    ['dot', '-Tpng', 'fcv_components/fcv_components.gv', '-O'])

subprocess.check_call(
    ['mv', 'fcv_components/fcv_components.gv.png', '00.-fcv_components.png'])

for i, line in enumerate(
        subprocess.check_output(['quilt', 'series']).decode().split('\n')):

    if not line.strip():
        break

    patch_name = line.split('/')[-1]

    subprocess.check_call(['quilt', 'push'])

    subprocess.check_call(
        ['dot', '-Tpng', 'fcv_components/fcv_components.gv', '-O'])

    subprocess.check_call(
        ['mv', 'fcv_components/fcv_components.gv.png',
         f'{patch_name}.png'])


subprocess.call(['quilt', 'pop', '-a'])
