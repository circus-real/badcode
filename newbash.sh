#!/bin/bash
relPath=$1
fName=$2

echo "entering target directory..."
cd $relPath
echo "creating file..."
file=touch "$fName.sh"
echo "adding exe permissions..."
chmod u+x $file
echo "done!"
