#!/bin/bash
sleep infinity & PID=$!
trap "kill $PID" INT TERM

echo starting
wait
echo exited
