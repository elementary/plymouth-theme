project(
    'io.elementary.plymouth-theme'
)

convert = run_command('which', 'convert')
if convert.returncode() != 0
    error('Please install imagemagick')
endif

meson.add_install_script('meson/post_install.py')
