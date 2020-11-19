#!/usr/bin/env python3
import os
import shutil
import subprocess

base_dir = os.environ.get('MESON_SOURCE_DIR', '.')

STEPS = 12
IMAGES_PER_STEP = 4
SIZE=38

SVG = os.path.join(base_dir, 'data', 'throbber.svg')

for i in range(0, STEPS):
    STEP_BASE_IMAGE = os.path.join(base_dir, 'elementary', 'throbber-{:04d}.png'.format(i * IMAGES_PER_STEP))

    subprocess.call([
        'convert',
        '-background',
        'none',
        SVG,
        STEP_BASE_IMAGE
    ])

    subprocess.call([
        'convert',
        '-background',
        'none',
        '-rotate',
        '{:d}'.format(i * 30),
        STEP_BASE_IMAGE,
        STEP_BASE_IMAGE
    ])

    subprocess.call([
        'convert',
        '-background',
        'none',
        '-gravity',
        'center',
        '-extent',
        '{:d}x{:d}'.format(SIZE, SIZE),
        STEP_BASE_IMAGE,
        STEP_BASE_IMAGE
    ])
    
    for j in range(1, IMAGES_PER_STEP):
        STEP_IMAGE = os.path.join(base_dir, 'elementary', 'throbber-{:04d}.png'.format(i * IMAGES_PER_STEP + j))
        shutil.copyfile(
            STEP_BASE_IMAGE,
            STEP_IMAGE
        )
