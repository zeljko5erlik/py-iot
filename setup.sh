sudo apt-get update

# In this desktop lite install many standard gui libaries aren't installed. This works 
# around the error: 
# Traceback (most recent call last):
#   File "/usr/bin/sense_emu_gui", line 9, in <module>
#     load_entry_point('sense-emu==1.1', 'gui_scripts', 'sense_emu_gui')()
#   File "/usr/lib/python3/dist-packages/pkg_resources/__init__.py", line 490, in load_entry_point
#     return get_distribution(dist).load_entry_point(group, name)
#   File "/usr/lib/python3/dist-packages/pkg_resources/__init__.py", line 2854, in load_entry_point
#     return ep.load()
#   File "/usr/lib/python3/dist-packages/pkg_resources/__init__.py", line 2445, in load
#     return self.resolve()
#   File "/usr/lib/python3/dist-packages/pkg_resources/__init__.py", line 2451, in resolve
#     module = __import__(self.module_name, fromlist=['__name__'], level=0)
#   File "/usr/lib/python3/dist-packages/sense_emu/gui.py", line 43, in <module>
#     gi.require_version('cairo', '1.0')
#   File "/usr/lib/python3/dist-packages/gi/__init__.py", line 129, in require_version
#     raise ValueError('Namespace %s not available' % namespace)
# ValueError: Namespace cairo not available
# https://stackoverflow.com/questions/69733848/unable-to-locate-package-python-gobject-in-ubuntu-21-10
sudo apt-get install -y software-properties-common python3-gi python3-gi-cairo gir1.2-gtk-3.0

# Install the Sense Emulation Software
sudo add-apt-repository -y ppa://waveform/ppa
sudo apt-get install -y python-sense-emu python3-sense-emu sense-emu-tools
