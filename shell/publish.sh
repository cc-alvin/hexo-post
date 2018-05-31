#!/usr/bin/env bash
# $1 is the root path of hexo
# $2 is the name of markdown mds
cp $2 $1/source/_post
cd $1
#hexo clean && hexo g
ls -alh