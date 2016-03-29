#!/bin/bash 
# 
if compgen -G runscripts.d/* > /dev/null; then 
    for file in runscripts.d/*; do
        if [[ -x $file ]]; then
            echo ... Executing $file
            $file
            echo
        fi
    done
fi

