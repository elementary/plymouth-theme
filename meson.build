project(
    'io.elementary.plymouth-theme',
    version: '6.0.0'
)

convert = find_program('convert')
python3 = find_program('python3', required: true)

run_command('mkdir', meson.build_root() / 'elementary', check: false)

rsvg = find_program('rsvg-convert')
run_command(
    rsvg, '--format', 'png',
    '--width=38', '--height=38',
    '--output', meson.project_build_root() / 'elementary' / 'throbber-0000.png',
    'elementary' / 'throbber.svg',
    check: true,
)

run_command(
    python3,
    'meson' / 'create_frames.py',
    check: true
)

install_subdir(
    'elementary',
    install_dir: get_option('datadir') / 'plymouth' / 'themes'
)

install_subdir(
    meson.project_build_root() / 'elementary',
    install_dir: get_option('datadir') / 'plymouth' / 'themes',
    strip_directory: false
)
