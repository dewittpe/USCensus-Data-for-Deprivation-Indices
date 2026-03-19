#!/bin/bash

set -euo pipefail

if [ "$#" -ne 2 ]; then
  echo "usage: $0 URL OUTPUT" >&2
  exit 2
fi

url="$1"
output="$2"

mkdir -p "$(dirname "$output")"

tmp="${output}.tmp"
err="${output}.err"
errlog="${err}.log"

rm -f "$tmp" "$err" "$errlog"

if curl \
  --silent \
  --show-error \
  --location \
  --fail-with-body \
  --retry 5 \
  --retry-delay 2 \
  --retry-connrefused \
  --retry-all-errors \
  --max-time 120 \
  "$url" \
  -o "$tmp" \
  2>"$errlog"
then
  if [ -s "$tmp" ]; then
    mv -f "$tmp" "$output"
    rm -f "$err" "$errlog"
    exit 0
  fi

  mv -f "$tmp" "$err"
  [ -s "$errlog" ] && cat "$errlog" >>"$err"
  rm -f "$errlog"
  exit 1
fi

if [ -s "$tmp" ]; then
  mv -f "$tmp" "$err"
  [ -s "$errlog" ] && cat "$errlog" >>"$err"
  rm -f "$errlog"
else
  mv -f "$errlog" "$err"
fi

exit 1
