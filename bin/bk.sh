#!/usr/bin/env bash

# Usage: bk.sh [testname]

set -e
set -x

VALGRIND="valgrind --tool=massif --pages-as-heap=yes"

if [ -z "$1" ] ; then
  # run all of the benchmarks in experiments/
  TESTS="experiments/exp*.py"
else
  # bk.sh testname; run experiments/exp[testname].py
  TESTS="experiments/exp$1.py"
fi

for i in $TESTS ; do
  echo "--- $i"
  $VALGRIND python3 $i
done
