#!/usr/bin/env python3
import os
import shutil
import subprocess

build_root = os.environ['MESON_BUILD_ROOT']
build_dir = os.path.join(build_root, 'elementary')

STEPS = 12
IMAGES_PER_STEP = 4
SIZE = 38

for i in range(0, STEPS):
    STEP_BASE_IMAGE = os.path.join(build_dir, 'throbber-{:04d}.png'.format(i * IMAGES_PER_STEP))

    try:
        shutil.copyfile(
            os.path.join(build_dir, 'throbber-0000.png'.format(i)),
            STEP_BASE_IMAGE
        )
    except shutil.SameFileError:
        pass

    subprocess.call([
        'convert',
        '-background',
        'none',
        '-rotate',
        '{:d}'.format(i * 30),
        STEP_BASE_IMAGE,
        STEP_BASE_IMAGE
    ])

    for j in range(1, IMAGES_PER_STEP):
        STEP_IMAGE = os.path.join(build_dir, 'throbber-{:04d}.png'.format(i * IMAGES_PER_STEP + j))
        shutil.copyfile(
            STEP_BASE_IMAGE,
            STEP_IMAGE
        )

for i in range(0, STEPS * IMAGES_PER_STEP):
    try:
        shutil.copyfile(
            os.path.join(build_dir, 'throbber-{:04d}.png'.format(i)),
            os.path.join(build_dir, 'animation-{:04d}.png'.format(i))
        )
    except shutil.SameFileError:
        pass
