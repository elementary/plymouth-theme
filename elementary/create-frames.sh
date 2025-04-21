#!/bin/bash

# Remove any extra symlinks/frames
for i in {0013..9999}; do rm -f animation-${i}.png; done
rm -f throbber-*.png

# Duplicate frames
for i in {0001..0024}
do
  ln -s animation-"$i".png animation-00$(( 10#$i + 12 )).png
done

# Create throbber symlinks
for frame in animation-*.png
do
  ln -s "$frame" "${frame/animation/throbber}"
done

