#!/bin/bash

# @author: Antonio Moreno. Script to run the minimum example project.

MAUDE=maude27

echo "===========================================================";
echo "---- EVALUATION MINIMUM EXAMPLE";
echo -e "===========================================================\n";

function evaluation() {
    results=$1".outputmaude"
    echo -n " - Running $1...";
    $MAUDE $1 &> $results
    echo -e "\r - Results for $1:";

    # python3 analysis/Main.py $1"results"$3"tu.outputmaude" $2 $3

    # rm $1"results"$3"tu.outputmaude";
    echo "";
}

evaluation evaluation/run_10tu.maude
